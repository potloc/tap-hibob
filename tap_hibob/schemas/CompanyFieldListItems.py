from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("list_id", th.StringType),
    th.Property("id", th.StringType),
    th.Property("value", th.StringType),
    th.Property("name", th.StringType),
    th.Property("archived", th.BooleanType)
).to_dict()
