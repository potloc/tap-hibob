from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("employee_id", th.StringType),
    th.Property("effectiveDate", th.StringType),
    th.Property("activeEffectiveDate", th.StringType),
    th.Property("endEffectiveDate", th.StringType),
    th.Property("modificationDate", th.StringType),
    th.Property("creationDate", th.StringType),
    th.Property("isCurrent", th.BooleanType),
    th.Property(
        "change",
        th.ObjectType(
            th.Property("reason", th.StringType),
            th.Property("changedBy", th.StringType),
            th.Property("changedById", th.StringType),
        ),
    ),
    th.Property("site", th.StringType),
    th.Property("title", th.StringType),
    th.Property("department", th.StringType),
    th.Property("workChangeType", th.StringType)
).to_dict()
