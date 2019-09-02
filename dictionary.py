#!/usr/bin/env python3
import cgi
import sys
import urllib.request
import urllib.parse

import cgitb
cgitb.enable()

sys.stdout.reconfigure(encoding='utf-8')
form = cgi.FieldStorage()
text = form.getvalue('word','')
if text != "":
    url = "https://jisho.org/api/v1/search/words?keyword=" + urllib.parse.quote(text)
    with urllib.request.urlopen(url) as res:
        print("Content-Type: text/plain; charset=utf-8")
        print("Access-Control-Allow-Origin: *\n")
        print(res.read().decode("utf-8"))