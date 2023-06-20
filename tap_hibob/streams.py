"""Stream type classes for tap-hibob."""

from pathlib import Path
import requests
from typing import Any, Dict, Optional, Union, List, Iterable
from datetime import date, datetime

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hibob.client import HibobStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

from tap_hibob.schemas import (
    CompanyFields,
    CompanyListByName,
    EmployeeEmploymentHistory,
    Employees,
    EmployeeTimeOff,
    EmployeePayroll,
    EmployeeWorkHistory
)


class EmployeesStream(HibobStream):
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
    schema = CompanyListByName.schema

    def get_child_context(self, record: dict, context: Optional[dict]):
        """Return a context dictionary for child streams."""
        return None
        if record.get("typeData").get("listId"):
            return {
                "list_id": record.get("typeData").get("listId")
            }

class CompanyListByNameStream(HibobStream):
    # https://apidocs.hibob.com/reference/get_company-named-lists-listname
    _LOG_REQUEST_METRIC_URLS=True
    name = "company_list_by_name"
    path = "/v1/company/named-lists/{list_id}"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    records_jsonpath = "$.values[*]"
    schema = CompanyListByName.schema
    parent_stream_type = CompanyFieldsStream