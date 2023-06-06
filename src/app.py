from config import load_config
from walk_directory_tree import walk_directory_tree
from utils.write_csv import write_csv


def main():
    config = load_config()
    changes = walk_directory_tree(config.path1, config.path2)
    write_csv(changes)


if __name__ == "__main__":
    main()
