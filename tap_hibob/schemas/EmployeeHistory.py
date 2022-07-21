from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("effectiveDate", th.DateType),
    th.Property("endEffectiveDate", th.DateType),
    th.Property("isCurrent", th.BooleanType),
    th.Property("canBeDeleted", th.BooleanType),
    th.Property(
        "change",
        th.ObjectType(
            th.Property("reason", th.StringType),
            th.Property("changedBy", th.StringType),
            th.Property("changedById", th.StringType),
        ),
    ),
    th.Property("creationDate", th.StringType),
    th.Property("modificationDate", th.DateType),
    th.Property("contract", th.StringType),
    th.Property("type", th.StringType),
    th.Property("calendarName", th.StringType),
    th.Property("calendarId", th.IntegerType),
    th.Property("flsaCode", th.IntegerType),
    th.Property("salaryPayType", th.StringType),
    th.Property("fte", th.IntegerType),
    th.Property("weeklyHours", th.IntegerType),
    th.Property("activeEffectiveDate", th.DateType),
    th.Property("employee_id", th.StringType),
).to_dict()
