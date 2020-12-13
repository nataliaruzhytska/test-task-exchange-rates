# test-task-exchange-rates

Build docker images
$ uid=$(id -u) gid=$(id -g) docker-compose build


Start compose
$ uid=$(id -u) gid=$(id -g) docker-compose up


Connect to the container
$ uid=$(id -u) gid=$(id -g) docker exec -ti exchange_rates_app_1 bash


Collect staticfiles
# exchange_rates/manage.py collectstatic --noinput


Apply migrations
# exchange_rates/manage.py migrate
# exchange_rates/manage.py migrate exchange_rates


Create super user
# exchange_rates/manage.py createsuperuser


Load fixtures from file (in container)
# exchange_rates/manage.py loaddata --format=json exchange_rates/exchange_rates/fixtures/init_data_currency.json


Run tests
# exchange_rates/manage.py test --keepdb


Homepage
# http://localhost:8000/exchange_rates/
