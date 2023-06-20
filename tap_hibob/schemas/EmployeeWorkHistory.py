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
    th.Property("customColumns",
        th.ObjectType("column_1644861659664", th.ArrayType(th.StringType)),
        th.ObjectType("column_1644862416222", th.ArrayType(th.StringType)),
        th.ObjectType("column_1664478354663", th.ArrayType(th.StringType)),
        th.ObjectType("column_1655996461265", th.StringType),
    ),
    th.Property("department", th.StringType),
    th.Property("workChangeType", th.StringType),
    th.Property("reportsTo",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("firstName", th.StringType),
            th.Property("surname", th.StringType),
            th.Property("email", th.StringType),
            th.Property("displayName", th.StringType),
        )
    )
).to_dict()
