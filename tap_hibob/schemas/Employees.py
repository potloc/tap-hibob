from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("companyId", th.IntegerType),
    th.Property("email", th.StringType),
    th.Property("fullName", th.StringType),
    th.Property("firstName", th.StringType),
    th.Property("surname", th.StringType),
    th.Property("displayName", th.StringType),
    th.Property("creationDateTime", th.StringType),
    th.Property(
        "work",
        th.ObjectType(
            th.Property(
                "durationofemployment",
                th.ObjectType(
                    th.Property("periodiso", th.StringType),
                    th.Property("sortfactor", th.IntegerType),
                    th.Property("humanize", th.StringType),
                ),
            ),
            th.Property("startdate", th.StringType),
            th.Property("manager", th.StringType),
            th.Property("reportstoidincompany", th.IntegerType),
            th.Property("employeeIdInCompany", th.IntegerType),
            th.Property("shortstartdate", th.StringType),
            th.Property("daysofpreviousservice", th.IntegerType),
            th.Property(
                "customcolumns",
                th.ObjectType(
                    th.Property("column_1655996461265", th.StringType),
                    th.Property(
                        "column_1644862416222",
                        th.ObjectType(
                            th.Property("value", th.StringType),
                        ),
                    ),
                    th.Property(
                        "column_1644861659664",
                        th.ObjectType(
                            th.Property("value", th.StringType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "custom",
                th.ObjectType(
                    th.Property("field_1651169416679", th.StringType),
                ),
            ),
            th.Property("directreports", th.IntegerType),
            th.Property("indirectreports", th.IntegerType),
            th.Property("tenureyears", th.IntegerType),
            th.Property("yearsofservice__it", th.IntegerType),
            th.Property("tenuredurationyears", th.NumberType),
            th.Property("tenuredurationyears_it", th.IntegerType),
            th.Property(
                "tenureduration",
                th.ObjectType(
                    th.Property("periodiso", th.StringType),
                    th.Property("sortfactor", th.IntegerType),
                    th.Property("humanize", th.StringType),
                ),
            ),
            th.Property(
                "reportsTo",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("email", th.StringType),
                    th.Property("firstName", th.StringType),
                    th.Property("surname", th.StringType),
                    th.Property("displayName", th.StringType),
                ),
            ),
            th.Property("department", th.StringType),
            th.Property("siteId", th.IntegerType),
            th.Property("isManager", th.BooleanType),
            th.Property("title", th.StringType),
            th.Property("site", th.StringType),
            th.Property("activeEffectiveDate", th.StringType),
            th.Property("yearsofservice", th.NumberType),
            th.Property("secondlevelmanager", th.NumberType),
        ),
    ),
    th.Property(
        "internal",
        th.ObjectType(
            th.Property(
                "periodSinceTermination",
                th.ObjectType(
                    th.Property("humanize", th.StringType),
                    th.Property("sortFactor", th.IntegerType),
                    th.Property("periodISO", th.StringType),
                ),
            ),
            th.Property("yearsSinceTermination", th.NumberType),
            th.Property("terminationReason", th.StringType),
            th.Property("probationEndDate", th.StringType),
            th.Property("currentActiveStatusStartDate", th.StringType),
            th.Property("terminationDate", th.StringType),
            th.Property("status", th.StringType),
            th.Property("terminationType", th.StringType),
            th.Property(
                "notice",
                th.ObjectType(
                    th.Property("length", th.IntegerType),
                    th.Property("unit", th.StringType),
                ),
            ),
            th.Property("lifecycleStatus", th.StringType),
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
                        "customcolumns",
                        th.ObjectType(
                            th.Property("column_1655996461265", th.StringType),
                            th.Property("column_1644862416222", th.StringType),
                            th.Property("column_1644861659664", th.StringType),
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
                    th.Property("periodSinceTermination", th.StringType),
                    th.Property("yearsSinceTermination", th.StringType),
                    th.Property("terminationReason", th.StringType),
                    th.Property("probationEndDate", th.StringType),
                    th.Property("currentActiveStatusStartDate", th.StringType),
                    th.Property("terminationDate", th.StringType),
                    th.Property("status", th.StringType),
                    th.Property("terminationType", th.StringType),
                    th.Property("notice", th.StringType),
                    th.Property("lifecycleStatus", th.StringType),
                ),
            ),
            th.Property(
                "about",
                th.ObjectType(
                    th.Property("superpowers", th.StringType),
                    th.Property("hobbies", th.StringType),
                    th.Property("avatar", th.StringType),
                    th.Property("about", th.StringType),
                    th.Property(
                        "socialdata",
                        th.ObjectType(
                            th.Property("linkedin", th.StringType),
                            th.Property("facebook", th.StringType),
                            th.Property("twitter", th.StringType),
                        ),
                    ),
                    th.Property(
                        "custom",
                        th.ObjectType(
                            th.Property("field_1645133202751", th.StringType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "personal",
                th.ObjectType(
                    th.Property("shortbirthdate", th.StringType),
                    th.Property("pronouns", th.StringType),
                    th.Property(
                        "custom",
                        th.ObjectType(
                            th.Property("field_1647463606890", th.StringType),
                            th.Property("field_1647619490812", th.StringType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "lifecycle",
                th.ObjectType(
                    th.Property(
                        "custom",
                        th.ObjectType(
                            th.Property("field_1651694080083", th.StringType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "payroll",
                th.ObjectType(
                    th.Property(
                        "employment",
                        th.ObjectType(
                            th.Property("siteworkingpattern", th.StringType),
                            th.Property("salarypaytype", th.StringType),
                            th.Property("actualworkingpattern", th.StringType),
                            th.Property("activeeffectivedate", th.StringType),
                            th.Property("workingpattern", th.StringType),
                            th.Property("fte", th.StringType),
                            th.Property("type", th.StringType),
                            th.Property("contract", th.StringType),
                            th.Property("calendarid", th.StringType),
                            th.Property("weeklyhours", th.StringType),
                        ),
                    ),
                ),
            ),
        ),
    ),
).to_dict()
