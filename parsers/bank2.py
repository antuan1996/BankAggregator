from parsers.base import BaseParser


class Bank2Parser(BaseParser):
    input_schema_path = "bank2Schema.json"

    def parse_format(self, df):
        return df.rename(columns={"amounts": "amount", "transaction": "type"})
