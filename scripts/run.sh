#!/bin/bash

# Ensure you have source the correct python before running

# DEBUG: 
# python manage.py runserver

# PRODUCTION: 
python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker
