import json
import os

from utils.pascal_to_snake import pascal_to_snake


def read_json(path: str, *args) -> dict:
    path = os.path.join(path, *args).replace("\\", "/")
    with open(path, encoding="utf-8-sig") as file:
        j = json.load(file, object_hook=pascal_to_snake)
    return j
