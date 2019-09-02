#!/usr/bin/env python3
import cgi
import sys
import urllib.request
import urllib.parse

import cgitb
cgitb.enable()

YAHOO_JAPAN_KEY   = "dj00aiZpPW9Qa29MNzBzR0JUaSZzPWNvbnN1bWVyc2VjcmV0Jng9Mzg-"
sys.stdout.reconfigure(encoding='utf-8')
form = cgi.FieldStorage()
text = form.getvalue('sentences','')
if text != "":
    url = "http://jlp.yahooapis.jp/MAService/V1/parse?appid=" + YAHOO_JAPAN_KEY + \
          "&results=ma&sentence=" + urllib.parse.quote(text) + \
          "&response=surface,reading,pos,baseform"
    with urllib.request.urlopen(url) as res:
        print("Content-Type: text/xml; charset=utf-8")
        print("Access-Control-Allow-Origin: *\n")
        print(res.read().decode("utf-8"))