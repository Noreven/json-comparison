from dataclasses import dataclass

from json_diff.utils.read_json import read_json


@dataclass
class JsonDiffConfig:
    path1: str
    path2: str


def load_config():
    config_path = "config.json"
    return JsonDiffConfig(**read_json(config_path))
