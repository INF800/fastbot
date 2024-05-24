#!/bin/bash

# By default dokku maps 5000 to 80 & 443
poetry run fastapi run fastbot/main.py --port 5000
