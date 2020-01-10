from pandas.io.json import build_table_schema
from pandas import DataFrame

from schemas import load_schema


def fields_list_to_frozenset(fields_list):
    items_list = []
    for field in fields_list:
        items = frozenset(field.items())
        items_list.append(items)
    return frozenset(items_list)


class BaseParser:
    input_schema_path = ""
    output_schema_path = "outputSchema.json"

    def __init__(self, df: DataFrame):
        self.df = df
        if not (self.input_schema_path and self.output_schema_path):
            raise ValueError("Empty value for input or output schema")
        self.input_schema = fields_list_to_frozenset(load_schema(self.input_schema_path))
        self.output_schema = fields_list_to_frozenset(load_schema(self.output_schema_path))

    @staticmethod
    def check_schema(df, schema):
        df_schema = build_table_schema(df, index=False, primary_key=None, version=False)
        df_schema = fields_list_to_frozenset(df_schema["fields"])
        return df_schema == schema

    def parse_format(self, df):
        return df

    def get_output(self):
        if not self.check_schema(self.df, self.input_schema):
            raise ValueError("Bad input format")
        df = self.parse_format(self.df)
        if not self.check_schema(df, self.output_schema):
            raise ValueError("Bad output format")
        return df
