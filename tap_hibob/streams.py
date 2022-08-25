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
    Employees,
    EmployeeHistory,
    EmployeeTimeOff,
    EmployeePayroll,
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


class EmployeeHistoryStream(HibobStream):
    name = "employee_history"
    path = "/v1/people/{employee_id}/employment"
    primary_keys = ["id", "employee_id"]
    records_jsonpath = "$.values[*]"
    replication_key = "creationDate"
    schema = EmployeeHistory.schema
    parent_stream_type = EmployeesStream
    ignore_parent_replication_keys = True


class EmployeeTimeOffStream(HibobStream):
    name = "employee_time_off"
    path = "/v1/timeoff/requests/changes"
    primary_keys = ["requestId"]
    records_jsonpath = "$.changes[*]"
    replication_key = "startDate"
    schema = EmployeeTimeOff.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["since"] = "2007-04-05T12:30-02:00"
        return params


class EmployeePayrollStream(HibobStream):
    name = "employee_payroll"
    path = "/v1/payroll/history"
    primary_keys = ["actual_payment_id", "id"]
    replication_method = "FULL_TABLE"
    records_jsonpath = "$.employees[*]"
    replication_key = "creationDate"
    schema = EmployeePayroll.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["showInactive"] = "false"
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        data = response.json()["employees"]
        ret = []

        for employee in data:
            elem = employee
            elem["actual_payment_id"] = elem["payroll"]["actualPayment"]["id"]
            ret.append(elem)

        return ret
