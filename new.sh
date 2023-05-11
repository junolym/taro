#!/bin/bash

cgi_name=$1
if [[ -z "$cgi_name" ]]; then
    echo 'required cgi_name'
    exit 1
fi

cgi="./taro/cgi-bin/$cgi_name"
conf="./taro/config/$cgi_name.toml"
if [[ -f "$cgi" || -f "$conf" ]]; then
    echo 'cgi exist'
else
    cp ./taro/template/cgi.py "$cgi"
    cp ./taro/template/config.toml "$conf"
fi

