"""REST client handling, including HibobStream base class."""

from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import requests
from singer_sdk.authenticators import APIKeyAuthenticator, BasicAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class HibobStream(RESTStream):
    """Hibob stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    records_jsonpath = "$[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.next_page"  # Or override `get_next_page_token`.

    @property
    def authenticator(self):
        """Return a new authenticator object."""
        if self.config.get("authorization", False):
            return APIKeyAuthenticator.create_for_stream(
                self,
                key="authorization",
                value=self.config.get("authorization"),
                location="header",
            )
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config.get("service_account_id"),
            password=self.config.get("service_account_password"),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            next_page_token = response.headers.get("X-Next-Page", None)

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row

    def backoff_max_tries(self) -> int:
        # https://sdk.meltano.com/en/latest/classes/singer_sdk.RESTStream.html#singer_sdk.RESTStream.backoff_max_tries
        # Default value is set to 5, making dynaminc
        # This is an exponential backoff - 2, 4, 8, 16, 32
        # -> Setting the number of retries allows us to circumvente rate limits.
        return self.config["backoff_max_tries"]
