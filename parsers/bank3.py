from time import strptime, strftime

from parsers.base import BaseParser


class Bank3Parser(BaseParser):
    input_schema_path = "bank3Schema.json"

    def format_date_column(self, val):
        parsed_date = strptime(val, "%d %b %Y")
        return strftime("%d-%m-%Y", parsed_date)

    def parse_format(self, df):
        df = df.rename(columns={"date_readable": "date"})
        df["date"] = df["date"].apply(self.format_date_column)
        df["amount"] = df["euro"] + df["cents"] / 100
        for name in ["euro", "cents"]:
            del df[name]
        return df
