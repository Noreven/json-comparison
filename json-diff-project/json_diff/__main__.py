import sys
from json_diff.config import load_config
from json_diff.walk_directory_tree import walk_directory_tree
from json_diff.utils.write_csv import write_csv


def main():
    args = sys.argv[1:]
    print(args)
    return
    config = load_config()
    changes = walk_directory_tree(config.path1, config.path2)
    write_csv(changes)


if __name__ == "__main__":
    main()
