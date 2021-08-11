#!/bin/bash

source .venv/bin/activate
cd learnwiki
exec python3 manage.py runserver localhost:9998
