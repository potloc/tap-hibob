from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("fullName", th.StringType),
    th.Property("creationDate", th.StringType),
    th.Property("displayName", th.StringType),
    th.Property("canBeDeleted", th.BooleanType),
    th.Property(
        "payroll",
        th.ObjectType(
            th.Property(
                "variablePayment",
                th.ObjectType(
                    th.Property("canBeDeleted", th.StringType),
                    th.Property(
                        "amount",
                        th.ObjectType(
                            th.Property("value", th.IntegerType),
                            th.Property("currency", th.StringType),
                        ),
                    ),
                    th.Property(
                        "change",
                        th.ObjectType(
                            th.Property("reason", th.StringType),
                            th.Property("changedBy", th.StringType),
                            th.Property("changedById", th.StringType),
                        ),
                    ),
                    th.Property("creationDate", th.StringType),
                    th.Property("individualPercent", th.StringType),
                    th.Property("variableType", th.StringType),
                    th.Property("isCurrent", th.StringType),
                    th.Property("modificationDate", th.StringType),
                    th.Property("id", th.IntegerType),
                    th.Property("paymentPeriod", th.StringType),
                    th.Property("effectiveDate", th.StringType),
                ),
            ),
            th.Property(
                "actualPayment",
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("payDate", th.StringType),
                    th.Property(
                        "change",
                        th.ObjectType(
                            th.Property("reason", th.StringType),
                            th.Property("changedBy", th.StringType),
                            th.Property("changedById", th.StringType),
                        ),
                    ),
                    th.Property(
                        "amount",
                        th.ObjectType(
                            th.Property("value", th.IntegerType),
                            th.Property("currency", th.StringType),
                        ),
                    ),
                    th.Property("payType", th.StringType),
                ),
            ),
            th.Property(
                "timeSinceLastSalaryChange",
                th.ObjectType(
                    th.Property("humanize", th.StringType),
                ),
            ),
            th.Property(
                "salary",
                th.ObjectType(
                    th.Property("canBeDeleted", th.StringType),
                    th.Property(
                        "change",
                        th.ObjectType(
                            th.Property("reason", th.StringType),
                            th.Property("changedBy", th.StringType),
                            th.Property("changedById", th.StringType),
                        ),
                    ),
                    th.Property("payFrequency", th.StringType),
                    th.Property("creationDate", th.StringType),
                    th.Property("isCurrent", th.StringType),
                    th.Property("modificationDate", th.StringType),
                    th.Property("payPeriod", th.StringType),
                    th.Property("id", th.IntegerType),
                    th.Property("endEffectiveDate", th.StringType),
                    th.Property("activeEffectiveDate", th.StringType),
                    th.Property("effectiveDate", th.StringType),
                    th.Property(
                        "base",
                        th.ObjectType(
                            th.Property("value", th.IntegerType),
                            th.Property("currency", th.StringType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "employmentType",
                th.ObjectType(
                    th.Property("canBeDeleted", th.StringType),
                    th.Property("weeklyHours", th.IntegerType),
                    th.Property(
                        "change",
                        th.ObjectType(
                            th.Property("reason", th.StringType),
                            th.Property("changedBy", th.StringType),
                            th.Property("changedById", th.StringType),
                        ),
                    ),
                    th.Property("contract", th.StringType),
                    th.Property("creationDate", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("isCurrent", th.StringType),
                    th.Property("modificationDate", th.StringType),
                    th.Property("salaryPayType", th.StringType),
                    th.Property("id", th.IntegerType),
                    th.Property("endEffectiveDate", th.StringType),
                    th.Property("activeEffectiveDate", th.StringType),
                ),
            ),
            th.Property(
                "deduction",
                th.ObjectType(
                    th.Property(
                        "Season ticket loans",
                        th.ObjectType(
                            th.Property("amount", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Cycle to work",
                        th.ObjectType(
                            th.Property("amount", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Company Car",
                        th.ObjectType(
                            th.Property("amount", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Childcare vouchers",
                        th.ObjectType(
                            th.Property("amount", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Lunch vouchers",
                        th.ObjectType(
                            th.Property("amount", th.IntegerType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "variable",
                th.ObjectType(
                    th.Property(
                        "227982853",
                        th.ObjectType(
                            th.Property("companyPercent", th.IntegerType),
                            th.Property(
                                "amount",
                                th.ObjectType(
                                    th.Property("value", th.IntegerType),
                                    th.Property("currency", th.StringType),
                                ),
                            ),
                            th.Property("paymentPeriod", th.IntegerType),
                            th.Property("individualPercent", th.IntegerType),
                            th.Property("departmentPercent", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Executive bonus",
                        th.ObjectType(
                            th.Property("companyPercent", th.IntegerType),
                            th.Property(
                                "amount",
                                th.ObjectType(
                                    th.Property("value", th.IntegerType),
                                    th.Property("currency", th.StringType),
                                ),
                            ),
                            th.Property("paymentPeriod", th.IntegerType),
                            th.Property("individualPercent", th.IntegerType),
                            th.Property("departmentPercent", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Bonus",
                        th.ObjectType(
                            th.Property("companyPercent", th.IntegerType),
                            th.Property(
                                "amount",
                                th.ObjectType(
                                    th.Property("value", th.IntegerType),
                                    th.Property("currency", th.StringType),
                                ),
                            ),
                            th.Property("paymentPeriod", th.IntegerType),
                            th.Property("individualPercent", th.IntegerType),
                            th.Property("departmentPercent", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "Commission",
                        th.ObjectType(
                            th.Property("companyPercent", th.IntegerType),
                            th.Property(
                                "amount",
                                th.ObjectType(
                                    th.Property("value", th.IntegerType),
                                    th.Property("currency", th.StringType),
                                ),
                            ),
                            th.Property("paymentPeriod", th.IntegerType),
                            th.Property("individualPercent", th.IntegerType),
                            th.Property("departmentPercent", th.IntegerType),
                        ),
                    ),
                    th.Property("contract", th.StringType),
                    th.Property("creationDate", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("isCurrent", th.StringType),
                    th.Property("modificationDate", th.StringType),
                    th.Property("salaryPayType", th.StringType),
                    th.Property("id", th.IntegerType),
                    th.Property("endEffectiveDate", th.StringType),
                    th.Property("activeEffectiveDate", th.StringType),
                ),
            ),
        ),
    ),
    th.Property("state", th.StringType),
).to_dict()
