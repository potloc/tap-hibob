from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.ArrayType(
    th.PropertiesList(
        th.Property("id", th.IntegerType)
    )
)


