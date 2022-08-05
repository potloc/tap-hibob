from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("requestId", th.IntegerType),
    th.Property("changeType", th.StringType),
    th.Property("startDate", th.StringType),
    th.Property("endDate", th.StringType),
    th.Property("startPortion", th.StringType),
    th.Property("endPortion", th.StringType),
    th.Property("policyTypeDisplayName", th.StringType),
    th.Property("employeeDisplayName", th.StringType),
    th.Property("employeeId", th.StringType),
    th.Property("type", th.StringType),
).to_dict()
