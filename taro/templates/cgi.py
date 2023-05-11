#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from lib.taro_comm import cgi_entry_plain


@cgi_entry_plain
def process(inputs, **req):
    for x in inputs:
        yield x


if __name__ == '__main__':
    process()
