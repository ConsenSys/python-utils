"""
    consensys_utils.flask.logging
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Flask logging resources


    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

import logging

from ..logging import IDFilter, create_logger as _create_logger
from ..utils import import_optional_module

flask = import_optional_module('flask')


class RequestIDFilter(IDFilter):
    """Logging filter that allows to enrich log with information related to the request"""

    def filter(self, record):
        """ Enrich log record with request ID"""

        if flask.has_request_context():  # pragma: no branch
            record.id = flask.request.id

        super().filter(record)

        return True


def create_logger(app, logger='app'):
    """Create logger for Flask app

    :param config: Logging configuration
    :type config: dict
    """

    # In case a config has been provided we use custom logger creation
    if 'logging' in app.config:
        _create_logger(app.config['logging'])
        return logging.getLogger(logger)

    # Otherwise classic flask logger creation
    else:
        return flask.logging.create_logger(app)