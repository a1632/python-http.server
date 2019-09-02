#!/usr/bin/env python3
import cgi
import os
import sys
import urllib.parse

import cgitb
cgitb.enable()

print("Content-Type: text/plain; charset=utf-8")
print("Access-Control-Allow-Origin: *\n")


sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
form = cgi.FieldStorage()
key = form.getvalue('key','')
if key != "":
    print('>>>>>>> error.py:key="'+urllib.parse.unquote(key)+'" <<<<<<<', file=sys.stderr)
    if not os.path.isfile(key):
        with open(key, mode='w') as f:
            contents = form.getvalue('contents','')
            if contents != "":
                f.write(contents)
