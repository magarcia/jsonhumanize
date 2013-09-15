#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    import ordereddict as collections
    import simplejson as json
else:
    import collections
    import json

from lxml.html.builder import TABLE, TH, TD, TR, CLASS, SPAN
import lxml.html


class JsonHuman(object):
    """Convert JSON to human readable HTML

    Process a JSON string and produce a styled HTML table for improve human
    readability.
    """

    def __init__(self, keep_order=False, **kwargs):
        super(JsonHuman, self).__init__(**kwargs)
        self.__keep_order = keep_order

    def __parse(self, json_obj, first=False):
        """Process a parsed JSON to HTML table"""

        if isinstance(json_obj, dict):
            type_class = 'jh-type-object'
            key_class = 'jh-object-key'
            value_class = 'jh-object-value'
            obj = json_obj.items()
        else:
            type_class = 'jh-type-array'
            key_class = 'jh-array-key'
            value_class = 'jh-array-value'
            obj = enumerate(json_obj)

        if first:
            type_class = "%s %s" % (type_class, 'jh-root')

        rows = []

        for key, value in obj:

            th = TH(
                CLASS('jh-key %s' % key_class),
                str(key)
            )

            if isinstance(value, bool):
                content = SPAN(
                    CLASS('jh-type-bool'),
                    ('true' if value else 'false')
                )

            elif isinstance(value, int):
                content = SPAN(
                    CLASS('jh-type-int jh-type-number'),
                    "%d" % value
                )

            elif isinstance(value, float):
                content = SPAN(
                    CLASS('jh-type-float jh-type-number'),
                    "%.2f" % value
                )

            elif hasattr(value, '__iter__'):
                content = self.__parse(value)

            else:
                content = SPAN(
                    CLASS('jh-type-string'),
                    '"%s"' % str(value)
                )

            td = TD(
                CLASS(value_class),
                content
            )

            rows.append(
                TR(
                    th,
                    td
                )
            )

        html = TABLE(
            CLASS(type_class),
            *rows
        )

        return html

    def format(self, json_string):
        """Process a JSON string to HTML table"""
        if self.__keep_order:
            json_obj = json.JSONDecoder(
                object_pairs_hook=collections.OrderedDict
            ).decode(json_string)
        else:
            json_obj = json.loads(json_string)

        html = ""

        html = self.__parse(json_obj, True)

        return lxml.html.tostring(html)
