#!/bin/sh

set -e


virtualenv oe-env
. ./oe-env/bin/activate
pip install -r openeats/OE2_Requirements.txt

mkdir -p db

cp settings_dev.py openeats/settings.py

./manage.py syncdb --all
./manage.py migrate --fake
./manage.py loaddata fixtures/navbar_about_data.json

./manage.py collectstatic
