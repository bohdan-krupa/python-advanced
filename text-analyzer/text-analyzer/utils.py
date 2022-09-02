import logging
import requests
from collections import namedtuple

Source = namedtuple('Source', ['type', 'value'])


def load_text_from_url(source: Source, source_logger: logging.Logger):
    try:
        res = requests.get(source.value)
        if res.status_code == 200:
            return res.text
        else:
            source_logger.error(
                f'Response from server not successful: {res.status_code}',
                extra=extra_params_for_logs(source),
            )
            return None
    except Exception as e:
        source_logger.error(
            f'Failed to connect to server: {e}',
            extra=extra_params_for_logs(source),
        )
        return None


def get_source_logger(name: str, log_level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    file_handler = logging.FileHandler('textanalyzer.log')
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s|%(type_of_resource)s|%(name_of_resource)s|%(message)s'
        )
    )
    logger.addHandler(file_handler)

    return logger


def extra_params_for_logs(source: Source):
    return {
        'type_of_resource': {'f': 'FILE', 'r': 'RESOURCE'}.get(source.type, 'UNKNOWN'),
        'name_of_resource': source.value,
    }
