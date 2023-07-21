"""Hibob tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_hibob.streams import (
    CompanyFieldListItems,
    CompanyFieldsStream,
    EmployeeEmploymentHistoryStream,
    EmployeePayrollStream,
    EmployeesStream,
    EmployeeTimeOffStream,
    EmployeeWorkHistoryStream,
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    CompanyFieldsStream,
    CompanyFieldListItems,
    EmployeesStream,
    EmployeeEmploymentHistoryStream,
    EmployeeTimeOffStream,
    EmployeePayrollStream,
    EmployeeWorkHistoryStream,
]


class TapHibob(Tap):
    """Hibob tap class."""

    name = "tap-hibob"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "authorization",
            th.StringType,
            required=False,
            description="Authorization token for Auth2.0",
        ),
        th.Property(
            "service_account_id",
            th.StringType,
            required=False,
            description="ID of service account.",
        ),
        th.Property(
            "service_account_password",
            th.StringType,
            required=False,
            description="Password for associated service account.",
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
        th.Property(
            "backoff_max_tries",
            th.IntegerType,
            default=5,
            description="""
                https://sdk.meltano.com/en/latest/classes/singer_sdk.RESTStream.html#singer_sdk.RESTStream.backoff_max_tries
                Default value is set to 5, making dynamic
                This is an exponential backoff - 2, 4, 8, 16, 32
                -> Setting the number of retries allows us to circumvente rate limits.
            """,
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapHibob.cli()
