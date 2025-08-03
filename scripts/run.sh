#!/bin/bash

# Ensure you have source the correct python before running

# python manage.py runserver
python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker