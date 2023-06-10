import os
import sys
from json_diff.walk_directory_tree import walk_directory_tree
from json_diff.utils.write_csv import write_csv


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        raise Exception("There should be only two path.")
    current_path = os.getcwd()
    path1, path2 = [os.sep.join([current_path, path]) for path in args]
    if not os.path.exists(path1) or not os.path.exists(path2):
        not_found_path = path1 if not os.path.exists(path1) else path2
        not_found_path = not_found_path.split(os.sep)[-1]
        raise Exception(f"{not_found_path} does not exist int this directory")
    changes = walk_directory_tree(path1, path2)
    write_csv(changes)


if __name__ == "__main__":
    main()
