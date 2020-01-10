
def serialize_to_csv(df, **kwargs):
    return df.to_csv(index=False, **kwargs)


OUTPUT_SERIALIZERS = {
    "csv": serialize_to_csv,
}


def serialize_output(df, output_format, **kwargs):
    if output_format not in OUTPUT_SERIALIZERS:
        raise KeyError("Output format is not implemented")
    serializer = OUTPUT_SERIALIZERS[output_format]
    return serializer(df, **kwargs)
