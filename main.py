import argparse

from output_serializers import serialize_output
from parsers import parse_file


def main():
    parser = argparse.ArgumentParser(description='Convert bank history format')
    parser.add_argument('input_file', help='path to input filename')
    parser.add_argument('output_file', help='path to output filename')
    parser.add_argument('input_format', help='input file format', choices=["bank1", "bank2", "bank3"])
    args = parser.parse_args()
    df = parse_file(args.input_file, args.input_format)
    serialize_output(df, "csv", path_or_buf=args.output_file)


if __name__ == '__main__':
    main()
