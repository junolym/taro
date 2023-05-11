#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import json
from io import StringIO


def cgi_entry_plain(func):

    def wrapper():
        resp = {}

        try:
            req = json.load(sys.stdin)
            req['input_str'] = req.get('input', '')
            req['inputs'] = req['input_str'].split('\n')
            req['input_buf'] = StringIO(req['input_str'])

            x = func(**req)

            if isinstance(x, str):
                resp['output'] = x
            elif isinstance(x, dict):
                resp = x
            elif x == None:
                resp['output'] = ''
            elif type(x) is StringIO:
                resp['output'] = x.getvalue()
            else:
                resp['output'] = ''
                for line in x:
                    resp['output'] += str(line) + '\n'

        except Exception as e:
            resp['error'] = str(e)

        print("Content-Type: application/json; charset=utf-8\n")
        print(json.dumps(resp))

    return wrapper
