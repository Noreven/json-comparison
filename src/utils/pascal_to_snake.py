import re


def pascal_to_snake(d: dict) -> dict:
    camel_dict = {
        re.sub(r"(?<!^)(?=[A-Z])", "_", key).lower(): value for key, value in d.items()
    }
    return camel_dict
