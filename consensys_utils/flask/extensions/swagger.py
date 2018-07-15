"""
    app.extensions.swagger
    ~~~~~~~~~~~~~~~~~~~~~~

    Declares swagger extension

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

from ...utils import import_optional_module

flasgger = import_optional_module('flasgger')


class Swagger(flasgger.Swagger):
    """Swagger extension"""

    def __init__(self, *args, template=None, openapi='3.0', version='0.1.0-dev', title='Base App', tags=None, **kwargs):
        template = template or {}
        template.setdefault('openapi', openapi)
        if title:
            template.setdefault('info', {'version': version, 'title': title, 'description': '{} API'.format(title)})
        template.setdefault('tags', tags or [])

        super().__init__(*args, template=template, **kwargs)


# Default swagger extension
swagger = Swagger()