from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("category", th.StringType),
    th.Property("name", th.StringType),
    th.Property("description", th.StringType),
    th.Property("jsonPath", th.StringType),
    th.Property("type", th.StringType),
    th.Property("typeData", th.ObjectType(
        th.Property("listId", th.StringType)
    )),
    th.Property("historical", th.BooleanType)
).to_dict()
