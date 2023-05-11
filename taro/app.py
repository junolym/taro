#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import rtoml
from flask import Flask, render_template, abort, request

application = Flask(__name__)
application.jinja_env.auto_reload = True
application.jinja_env.trim_blocks = True
application.jinja_env.lstrip_blocks = True


def get_config(cgi_path):
    def wrapper(cgi):
        config = {}
        config_path = f'config/{cgi_path}/{cgi}.toml'
        if os.path.isfile(config_path):
            with open(config_path, encoding='utf-8') as f:
                config = rtoml.load(f)
        config['cgi'] = cgi
        return config

    return wrapper


@application.route('/')
@application.route('/<path:path>/')
def process(path=''):
    cgi_path = f'cgi-bin/{path}'
    if os.path.isdir(cgi_path):
        cgi_list = sorted(os.listdir(cgi_path))
        return render_template('index.html', cgi_list=map(get_config(path), cgi_list))

    if os.path.isfile(cgi_path):
        cgi = os.path.basename(path)
        dirname = os.path.dirname(path)
        return render_template('cgi.html', **get_config(dirname)(cgi), path=path)

    abort(404)
