import filecmp
import os

from json_diff.classes.json_diff import JsonDiff
from json_diff.utils.read_json import read_json


def walk_directory_tree(path1: str, path2: str, changes: list = []):
    dir_diff = filecmp.dircmp(path1, path2)
    for dir_ in dir_diff.common:
        if os.path.isfile(f"{path1}/{dir_}"):
            j1 = read_json(path1, dir_)
            j2 = read_json(path2, dir_)
            json_diff = JsonDiff()
            json_diff.json_diff(j1, j2)

            for result in json_diff.results:
                changes.append(
                    {
                        "Path": path1,
                        "File": dir_,
                        "Type": result.action,
                        "Attribute": result.attribute,
                        "Ref": result.ref,
                        "Change": result.change,
                    }
                )
        else:
            walk_directory_tree(f"{path1}/{dir_}", f"{path2}/{dir_}", changes)
    for dir_ in dir_diff.right_only:
        changes.append(
            {
                "Path": path2,
                "File": dir_,
                "Type": "CREATED",
                "Attribute": "",
                "Ref": "",
                "Change": "",
            }
        )
    for dir_ in dir_diff.left_only:
        changes.append(
            {
                "Path": path1,
                "File": dir_,
                "Type": "DELETED",
                "Attribute": "",
                "Ref": "",
                "Change": "",
            }
        )
    return changes
