from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("companyId", th.IntegerType),
    th.Property("email", th.StringType),
    th.Property("fullName", th.StringType),
    th.Property("firstName", th.StringType),
    th.Property("surname", th.StringType),
    th.Property("displayName", th.StringType),
    th.Property("creationDateTime", th.DateTimeType),
    th.Property("work",
        th.ObjectType(
            th.Property("start_date", th.DateTimeType),
            th.Property("manager", th.StringType),
            th.Property("reportsToIdInComany", th.IntegerType),
            th.Property("employeeIdInCompany", th.IntegerType),
            th.Property("reportsTo",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("email", th.StringType),
                    th.Property("firstName", th.StringType),
                    th.Property("surname", th.StringType),
                    th.Property("displayName", th.StringType),
                )
            ),
            th.Property("department", th.StringType),
            th.Property("siteId", th.IntegerType),
            th.Property("isManager", th.BooleanType),
            th.Property("title", th.StringType),
            th.Property("site", th.StringType),

        )
    ),
    th.Property("internal",
        th.ObjectType(
            th.Property("periodSinceTermination",
                th.ObjectType(
                    th.Property("humanize", th.StringType),
                    th.Property("sortFactor", th.IntegerType),
                    th.Property("periodISO", th.StringType),
                )
            ),
            th.Property("yearsSinceTermination", th.NumberType),
            th.Property("terminationReason", th.StringType),
            th.Property("probationEndDate", th.DateType),
            th.Property("currentActiveStatusStartDate", th.DateType),
            th.Property("terminationDate", th.DateType),
            th.Property("status", th.StringType),
            th.Property("terminationType", th.StringType),
            th.Property("notice",
                th.ObjectType(
                    th.Property("length", th.IntegerType),
                    th.Property("unit", th.StringType),
                )
            ),
            th.Property("lifecycleStatus", th.StringType),
        )
    ),
).to_dict()

