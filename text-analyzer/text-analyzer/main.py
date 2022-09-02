import argparse
from text_analyzer import TextAnalyzer
import concurrent.futures
from utils import Source, load_text_from_url, get_source_logger, extra_params_for_logs

source_logger = get_source_logger(__name__)


def analyze(source: Source) -> None:
    source_logger.info('Started getting text', extra=extra_params_for_logs(source))

    if source.type == 'r':
        text = load_text_from_url(source)
    elif source.type == 'f':
        with open(source.value, 'r') as file:
            text = file.read()

    source_logger.info('Got the text', extra=extra_params_for_logs(source))

    if text:
        source_logger.info(
            'Started analyze the text', extra=extra_params_for_logs(source)
        )
        print(TextAnalyzer(text))
        source_logger.info(
            'Finished analyze the text', extra=extra_params_for_logs(source)
        )
    else:
        source_logger.error('There is no text', extra=extra_params_for_logs(source))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text analyzer CLI', add_help=True)
    parser.add_argument('-f', action='store', nargs='*', help='File to read')
    parser.add_argument('-r', action='store', nargs='*', help='Resource to read')
    args = vars(parser.parse_args())

    sources = [
        Source(flag, value) for flag in args if args[flag] for value in args[flag]
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(lambda source: analyze(source), sources)
