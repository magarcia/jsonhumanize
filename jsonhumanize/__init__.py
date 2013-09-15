#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Martin Garcia'
__email__ = 'newluxfero@gmail.com'
__version__ = '0.1.1'

from .jsonhumanize import JsonHuman


def main():
    import argparse
    import os
    import shutil
    from lxml.html.builder import HTML, HEAD, LINK, BODY, TITLE
    import lxml.html

    parser = argparse.ArgumentParser(
        description='Convert JSON to human readable HTML'
    )

    parser.add_argument('jsonfile', metavar='JSONFILE', type=str,
                        help='file with json to be processed')

    parser.add_argument('-k', '--keep_order', dest='keep_order',
                        action='store_true', default=False,
                        help='keep json order in the result')

    parser.add_argument('-o', '--output', dest='output', default=False,
                        type=str, help='generate html document')

    args = parser.parse_args()

    json_string = open(args.jsonfile, 'r').read()
    html = JsonHuman(keep_order=args.keep_order).format(json_string)

    if args.output:
        filepath, extension = os.path.splitext(args.output)

        html_output = open(args.output, 'w')
        css_output = "%s.css" % filepath
        css_source = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'jsonhuman.css'
        )

        html = HTML(
            HEAD(
                LINK(
                    rel="stylesheet",
                    href=os.path.basename(css_output),
                    type="text/css"
                ),
                TITLE("JsonHuman")
            ),
            BODY(
                lxml.html.fromstring(html)
            )
        )

        html_output.write(lxml.html.tostring(html))
        html_output.close()
        shutil.copyfile(css_source, css_output)

    else:
        print(html)

if __name__ == "__main__":
    main()
