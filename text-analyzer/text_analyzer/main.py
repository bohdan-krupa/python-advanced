import argparse
import concurrent.futures
from text_processor import Source
from text_processor import TextProcessor
from db.repository import Repository


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text analyzer CLI", add_help=True)
    parser.add_argument("-f", action="store", nargs="*", help="File to read")
    parser.add_argument("-r", action="store", nargs="*", help="Resource to read")
    parser.add_argument("--view", action="store", nargs="*", help="Resource to read")
    args = vars(parser.parse_args())

    sources = [
        Source(flag, value) for flag in args if args[flag] for value in args[flag]
    ]

    repository = Repository()

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(
            lambda source: TextProcessor(source, repository).analyze(), sources
        )
