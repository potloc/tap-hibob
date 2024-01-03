"""Hibob tap class."""

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_hibob import streams

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

    def discover_streams(self) -> list[streams.HibobStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CompanyFieldsStream(self),
            streams.CompanyFieldListItems(self),
            streams.EmployeesStream(self),
            streams.EmployeeEmploymentHistoryStream(self),
            streams.EmployeeTimeOffStream(self),
            streams.EmployeePayrollStream(self),
            streams.EmployeeWorkHistoryStream(self),
            streams.EmployeesSearchStream(self),
        ]
