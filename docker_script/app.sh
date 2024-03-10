#!/bin/bash

sleep 10

cd src

python manage.py migrate
python manage.py loaddata fixtures/hubs/data.json
python manage.py loaddata fixtures/users/superuser.json

python manage.py runserver 0.0.0.0:8000


