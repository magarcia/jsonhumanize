#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jsonhumanize
----------------------------------

Tests for `jsonhumanize` module.
"""

import unittest

from jsonhumanize import JsonHuman


class TestJsonhumanize(unittest.TestCase):
    """
    Test class for jsonhumanize module.
    """

    def setUp(self):
        self.json = '''{
          "name": "jsonhumanize",
          "description": "Convert JSON to human readable HTML",
          "author": "Martin Garcia <newluxfero@gmail.com>",
          "tags": ["DOM", "HTML", "JSON", "Pretty Print"],
          "version": "0.1.0",
          "main": "jsonhumanize.py",
          "license" : "MIT",
          "dependencies": {
              "crel": "1.0.0"
          },
          "repository": {
            "type": "git",
            "url": "git://github.com/magarcia/jsonhumanize.git"
          },
          "bugs": {
            "url": "http://github.com/magarcia/jsonhumanize/issues"
          },
          "contributors": [],
          "config": {
            "what?": "this object is just to show some extra stuff",
            "how?": ["use jsonhumanize", "add jsonhumanize.css", "???", \
"profit!"],
            "customization?": ["customize the css prefix", "change the css \
file"],
            "integer": 42,
            "float": 12.3,
            "bool": true
          }
        }'''

        self.html = '<table class="jh-type-object jh-root"><tr>\
<th class="jh-key jh-object-key">name</th><td class="jh-object-value">\
<span class="jh-type-string">"jsonhumanize"</span></td></tr><tr>\
<th class="jh-key jh-object-key">description</th>\
<td class="jh-object-value"><span class="jh-type-string">\
"Convert JSON to human readable HTML"</span></td></tr><tr>\
<th class="jh-key jh-object-key">author</th>\
<td class="jh-object-value"><span class="jh-type-string">\
"Martin Garcia &lt;newluxfero@gmail.com&gt;"</span></td></tr><tr>\
<th class="jh-key jh-object-key">tags</th><td class="jh-object-value">\
<table class="jh-type-array"><tr><th class="jh-key jh-array-key">0\
</th><td class="jh-array-value"><span class="jh-type-string">"DOM"\
</span></td></tr><tr><th class="jh-key jh-array-key">1</th><td \
class="jh-array-value"><span class="jh-type-string">"HTML"</span></td>\
</tr><tr><th class="jh-key jh-array-key">2</th>\
<td class="jh-array-value"><span class="jh-type-string">"JSON"</span>\
</td></tr><tr><th class="jh-key jh-array-key">3</th>\
<td class="jh-array-value"><span class="jh-type-string">"Pretty Print"\
</span></td></tr></table></td></tr><tr>\
<th class="jh-key jh-object-key">version</th>\
<td class="jh-object-value"><span class="jh-type-string">"0.1.0"\
</span></td></tr><tr><th class="jh-key jh-object-key">main</th>\
<td class="jh-object-value"><span class="jh-type-string">\
"jsonhumanize.py"</span></td></tr><tr><th class="jh-key \
jh-object-key">license</th><td class="jh-object-value">\
<span class="jh-type-string">"MIT"</span></td></tr><tr>\
<th class="jh-key jh-object-key">dependencies\
</th><td class="jh-object-value"><table class="jh-type-object"><tr>\
<th class="jh-key jh-object-key">crel</th><td class="jh-object-value">\
<span class="jh-type-string">"1.0.0"</span></td></tr></table></td>\
</tr><tr><th class="jh-key jh-object-key">repository</th>\
<td class="jh-object-value"><table class="jh-type-object"><tr>\
<th class="jh-key jh-object-key">type</th><td class="jh-object-value">\
<span class="jh-type-string">"git"</span></td></tr><tr>\
<th class="jh-key jh-object-key">url</th><td class="jh-object-value">\
<span class="jh-type-string">\
"git://github.com/magarcia/jsonhumanize.git"</span></td></tr></table>\
</td></tr><tr><th class="jh-key jh-object-key">bugs</th>\
<td class="jh-object-value"><table class="jh-type-object"><tr>\
<th class="jh-key jh-object-key">url</th><td class="jh-object-value">\
<span class="jh-type-string">\
"http://github.com/magarcia/jsonhumanize/issues"</span></td></tr>\
</table></td></tr><tr><th class="jh-key jh-object-key">contributors\
</th><td class="jh-object-value"><table class="jh-type-array"></table>\
</td></tr><tr><th class="jh-key jh-object-key">config</th>\
<td class="jh-object-value"><table class="jh-type-object"><tr>\
<th class="jh-key jh-object-key">what?</th>\
<td class="jh-object-value"><span class="jh-type-string">\
"this object is just to show some extra stuff"</span></td></tr><tr>\
<th class="jh-key jh-object-key">how?</th><td class="jh-object-value">\
<table class="jh-type-array"><tr><th class="jh-key jh-array-key">0\
</th><td class="jh-array-value"><span class="jh-type-string">\
"use jsonhumanize"</span></td></tr><tr>\
<th class="jh-key jh-array-key">1</th><td class="jh-array-value">\
<span class="jh-type-string">"add jsonhumanize.css"</span></td></tr>\
<tr><th class="jh-key jh-array-key">2</th><td class="jh-array-value">\
<span class="jh-type-string">"???"</span></td></tr><tr>\
<th class="jh-key jh-array-key">3</th><td class="jh-array-value">\
<span class="jh-type-string">"profit!"</span></td></tr></table></td>\
</tr><tr><th class="jh-key jh-object-key">customization?</th>\
<td class="jh-object-value"><table class="jh-type-array"><tr>\
<th class="jh-key jh-array-key">0</th><td class="jh-array-value">\
<span class="jh-type-string">"customize the css prefix"</span></td>\
</tr><tr><th class="jh-key jh-array-key">1</th>\
<td class="jh-array-value"><span class="jh-type-string">\
"change the css file"</span></td></tr></table></td></tr><tr>\
<th class="jh-key jh-object-key">integer</th>\
<td class="jh-object-value"><span class="jh-type-int jh-type-number">\
42</span></td></tr><tr><th class="jh-key jh-object-key">float</th>\
<td class="jh-object-value">\
<span class="jh-type-float jh-type-number">12.30</span></td></tr><tr>\
<th class="jh-key jh-object-key">bool</th><td class="jh-object-value">\
<span class="jh-type-bool">true</span></td></tr></table></td></tr>\
</table>'

    def test_something(self):
        parsed = JsonHuman(keep_order=True).format(self.json)
        self.assertEqual(parsed, self.html)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
