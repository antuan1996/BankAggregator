import pandas

from .bank1 import Bank1Parser
from .bank2 import Bank2Parser
from .bank3 import Bank3Parser


PARSERS_MAP = {
    "bank1": Bank1Parser,
    "bank2": Bank2Parser,
    "bank3": Bank3Parser
}


def load_parser(key):
    if key in PARSERS_MAP:
        return PARSERS_MAP[key]
    else:
        raise KeyError("Parser for given key is not presented")


def parse_file(path, format_key):
    df = pandas.read_csv(path)
    parser_cls = load_parser(format_key)
    return parser_cls(df).get_output()
