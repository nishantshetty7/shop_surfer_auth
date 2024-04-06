#!/bin/sh

gunicorn shop_surfer_auth.wsgi:application -b 0.0.0.0:80