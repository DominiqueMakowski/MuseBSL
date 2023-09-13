import argparse
import sys

from .cli import CLI


def main():
    parser = argparse.ArgumentParser(
        description="Stream and visualize data from the Muse EEG headset.",
        usage="""MuseBSL <command> [<args>]
        """,
    )

    parser.add_argument("command", help="Command to run.")

    # parse_args defaults to [1:] for args, but you need to
    # exclude the rest of the args too, or validation will fail
    args = parser.parse_args(sys.argv[1:2])

    if not hasattr(CLI, args.command):
        print("Incorrect usage. See help below.")
        parser.print_help()
        exit(1)

    CLI(args.command)


if __name__ == "__main__":
    main()
