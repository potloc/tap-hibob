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
    th.Property(
        "internal",
        th.ObjectType(
            th.Property("terminationReason", th.StringType),
            th.Property("probationEndDate", th.StringType),
            th.Property("terminationDate", th.StringType),
        ),
    ),
    th.Property(
        "work",
        th.ObjectType(
            th.Property(
                "customColumns",
                th.ObjectType(
                    th.Property("column_1655996461265", th.StringType),
                    th.Property("column_1644862416222", th.ArrayType(th.StringType)),
                    th.Property("column_1644861659664", th.ArrayType(th.StringType)),
                ),
            ),
            th.Property(
                "custom",
                th.ObjectType(
                    th.Property("field_1651169416679", th.StringType),
                ),
            ),
            th.Property("department", th.StringType),
            th.Property("isManager", th.BooleanType),
            th.Property("title", th.StringType),
            th.Property("site", th.StringType),
        ),
    ),
    th.Property(
        "humanReadable",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("companyId", th.StringType),
            th.Property("email", th.StringType),
            th.Property("fullName", th.StringType),
            th.Property("firstName", th.StringType),
            th.Property("surname", th.StringType),
            th.Property("displayName", th.StringType),
            th.Property("creationDateTime", th.StringType),
            th.Property("avatarurl", th.StringType),
            th.Property("secondname", th.StringType),
            th.Property(
                "work",
                th.ObjectType(
                    th.Property("startdate", th.StringType),
                    th.Property("shortstartdate", th.StringType),
                    th.Property("manager", th.StringType),
                    th.Property("reportsToIdInComany", th.IntegerType),
                    th.Property("employeeIdInCompany", th.StringType),
                    th.Property("reportsTo", th.StringType),
                    th.Property("department", th.StringType),
                    th.Property("siteId", th.StringType),
                    th.Property("isManager", th.StringType),
                    th.Property("title", th.StringType),
                    th.Property("site", th.StringType),
                    th.Property("durationofemployment", th.StringType),
                    th.Property("daysofpreviousservice", th.StringType),
                    th.Property("directreports", th.StringType),
                    th.Property("tenureduration", th.StringType),
                    th.Property("activeeffectivedate", th.StringType),
                    th.Property("tenuredurationyears", th.StringType),
                    th.Property("yearsofservice", th.StringType),
                    th.Property("secondlevelmanager", th.StringType),
                    th.Property("indirectreports", th.StringType),
                    th.Property("tenureyears", th.StringType),
                    th.Property(
                        "customColumns",
                        th.ObjectType(
                            th.Property("column_1655996461265", th.StringType),
                            th.Property(
                                "column_1644862416222", th.ArrayType(th.StringType)
                            ),
                            th.Property(
                                "column_1644861659664", th.ArrayType(th.StringType)
                            ),
                        ),
                    ),
                    th.Property(
                        "custom",
                        th.ObjectType(
                            th.Property("field_1651169416679", th.StringType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "internal",
                th.ObjectType(
                    th.Property("terminationReason", th.StringType),
                    th.Property("probationEndDate", th.StringType),
                    th.Property("terminationDate", th.StringType),
                ),
            ),
            th.Property(
                "personal",
                th.ObjectType(
                    th.Property("pronouns", th.StringType),
                ),
            ),
            th.Property(
                "payroll",
                th.ObjectType(
                    th.Property(
                        "employment",
                        th.ObjectType(
                            th.Property("type", th.StringType),
                            th.Property("contract", th.StringType),
                        ),
                    ),
                ),
            ),
        ),
    ),
).to_dict()
