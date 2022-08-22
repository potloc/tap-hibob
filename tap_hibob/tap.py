"""Hibob tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_hibob.streams import (
    EmployeesStream,
    EmployeeHistoryStream,
    EmployeeTimeOffStream,
    EmployeePayrollStream,
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    EmployeesStream,
    EmployeeHistoryStream,
    EmployeeTimeOffStream,
    EmployeePayrollStream,
]


class TapHibob(Tap):
    """Hibob tap class."""

    name = "tap-hibob"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "authorization",
            th.StringType,
            required=True,
            description="Authorization token for Auth2.0",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.hibob.com",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapHibob.cli()
