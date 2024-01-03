"""Stream type classes for tap-hibob."""

from pathlib import Path
import requests
from requests import Response
from typing import Any, Dict, Optional, Iterable


from tap_hibob.client import HibobStream

from tap_hibob.schemas import (
    CompanyFieldListItems,
    CompanyFields,
    EmployeeEmploymentHistory,
    Employees,
    EmployeeTimeOff,
    EmployeePayroll,
    EmployeeWorkHistory
)

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class EmployeesStream(HibobStream):
    # Will be deprecated by March 2024. See here: https://apidocs.hibob.com/reference/get_people
    """Define custom stream."""

    name = "employees"
    path = "/v1/people"
    primary_keys = ["id"]
    records_jsonpath = "$.employees[*]"
    replication_method = "INCREMENTAL"
    replication_key = "creationDateTime"
    schema = Employees.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["showInactive"] = "true"
        params["includeHumanReadable"] = "true"
        return params

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "employee_id": record["id"],
        }

class EmployeesSearchStream(HibobStream):
    # https://apidocs.hibob.com/reference/post_people-search
    """
        This API returns a list of requested employees with requested fields.
        The data is filtered based on the requested fields and access level of the logged-in user.
        Only viewable categories are returned.
        Supported user types: Service.
    """

    name = "employees_search"
    path = "/v1/people/search"
    primary_keys = ["id"]
    records_jsonpath = "$.employees[*]"
    replication_method = "INCREMENTAL"
    replication_key = "creationDateTime"
    rest_method = "POST"
    schema = Employees.schema

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        return {
            "fields":[
                "/root/displayName",
                "/root/firstName",
                "/root/fullName",
                "/root/surname",
                "/root/email",
                "/root/creationDateTime",
                "/personal/pronouns",
                "/payroll/employment/type",
                "/payroll/employment/contract",
                "/work/customColumns/column_1644862416222",
                "/work/customColumns/column_1644861659664",
                "/work/custom/field_1651169416679",
                "/work/title",
                "/work/site",
                "/work/department",
                "/internal/terminationReason",
                "/internal/probationEndDate",
                "/internal/terminationDate"
            ],
            "showInactive": True,
            "humanReadable": "APPEND"
        }

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "employee_id": record["id"],
        }

# TODO - Replace by employee_employment_history https://potloc.atlassian.net/browse/DE-498
class EmployeeEmploymentHistoryStream(HibobStream):
    name = "employee_history"
    path = "/v1/people/{employee_id}/employment"
    primary_keys = ["id", "employee_id"]
    records_jsonpath = "$.values[*]"
    replication_key = None
    state_partitioning_keys = []
    schema = EmployeeEmploymentHistory.schema
    parent_stream_type = EmployeesStream
    ignore_parent_replication_keys = True
    employee_id = ""

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = super().get_url_params(context, next_page_token)
        self.employee_id = context["employee_id"]
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        data = response.json()["values"]
        ret = []
        for e in data:
            elem = e
            elem["employee_id"] = self.employee_id
            ret.append(elem)

        return ret


class EmployeeWorkHistoryStream(HibobStream):
    name = "employee_work_history"
    path = "/v1/people/{employee_id}/work"
    primary_keys = ["id", "employee_id"]
    records_jsonpath = "$.values[*]"
    replication_key = None
    state_partitioning_keys = []
    schema = EmployeeWorkHistory.schema
    parent_stream_type = EmployeesStream
    ignore_parent_replication_keys = True
    employee_id = ""

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = super().get_url_params(context, next_page_token)
        self.employee_id = context["employee_id"]
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        data = response.json()["values"]
        ret = []
        for e in data:
            elem = e
            elem["employee_id"] = self.employee_id
            ret.append(elem)

        return ret


class EmployeeTimeOffStream(HibobStream):
    name = "employee_time_off"
    path = "/v1/timeoff/requests/changes"
    primary_keys = ["requestId"]
    records_jsonpath = "$.changes[*]"
    replication_key = None
    state_partitioning_keys = []
    schema = EmployeeTimeOff.schema
    ignore_parent_replication_keys = True

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["since"] = "2007-04-05T12:30-02:00"
        return params


class EmployeePayrollStream(HibobStream):
    name = "employee_payroll"
    path = "/v1/payroll/history"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    records_jsonpath = "$.employees[*]"
    replication_key = "creationDate"
    schema = EmployeePayroll.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["showInactive"] = "true"
        return params

class CompanyFieldsStream(HibobStream):
    # https://apidocs.hibob.com/reference/get_company-people-fields
    name = "company_fields"
    path = "/v1/company/people/fields"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    records_jsonpath = "$.[*]"
    schema = CompanyFields.schema

    def get_child_context(self, record: dict, context: Optional[dict]):
        """Return a context dictionary for child streams."""
        if record.get("typeData").get("listId"):
            return {
                "list_id": record.get("typeData").get("listId")
            }
        return None

class CompanyFieldListItems(HibobStream):
    # https://apidocs.hibob.com/reference/get_company-named-lists-listname
    name = "company_field_list_items"
    path = "/v1/company/named-lists/{list_id}"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    records_jsonpath = "$.values[*]"
    schema = CompanyFieldListItems.schema
    parent_stream_type = CompanyFieldsStream
    list_id = ""

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = super().get_url_params(context, next_page_token)
        self.list_id = context.get("list_id")
        return params


    def parse_response(self, response: Response) -> Iterable[dict]:
        data = response.json().get("values")
        ret = []
        for e in data:
            elem = e
            elem["list_id"] = self.list_id
            elem["id"] = str(elem["id"])
            ret.append(elem)
        return ret