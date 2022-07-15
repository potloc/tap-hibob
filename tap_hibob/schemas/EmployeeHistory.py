from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("effectiveDate", th.DateTimeType),
    th.Property("modificationDate", th.StringType),
    th.Property("employee_id", th.StringType),
).to_dict()
