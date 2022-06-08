"""Stream type classes for tap-hibob."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hibob.client import HibobStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

from tap_hibob.schemas import Employees

class EmployeesStream(HibobStream):
    _LOG_REQUEST_METRIC_URLS=True
    """Define custom stream."""
    name = "employees"
    path = "/v1/people"
    primary_keys = ["id"]
    records_jsonpath = "$.employees[*]"
    replication_key = "creationDateTime"
    schema = Employees.schema

    def get_url_params(self, context: Optional[dict], next_page_token: Optional[Any]) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["showInactive"] = True
        return params



