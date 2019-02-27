import sys

import shell


def main() -> None:
    try:
        if sys.argv[1:]:
            return shell.fparse(sys.argv[1])
        print('Type "quit" to exit the program.')
        return shell.stdin_parse()
    except (EOFError, KeyboardInterrupt):
        exit("Goodbye !")


if __name__ == "__main__":
    main()
