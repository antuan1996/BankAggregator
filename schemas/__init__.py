import json
from os.path import join


def load_schema(filename):
    path = join("./schemas", filename)
    fd = open(path, "r")
    return json.load(fd)
