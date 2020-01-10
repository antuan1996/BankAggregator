from time import strftime, strptime

from parsers.base import BaseParser


class Bank1Parser(BaseParser):
    input_schema_path = "bank1Schema.json"

    def format_date_column(self, val):
        parsed_date = strptime(val, "%b %d %Y")
        return strftime("%d-%m-%Y", parsed_date)

    def parse_format(self, df):
        df = df.rename(columns={"timestamp": "date"})
        df["date"] = df["date"].apply(self.format_date_column)
        return df
