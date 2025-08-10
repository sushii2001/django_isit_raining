#!/usr/bin/env bash
python manage.py check
python manage.py test homepage --noinput --keepdb
