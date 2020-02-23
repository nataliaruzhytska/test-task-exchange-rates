# test-task-exchange-rates

Build docker images
$ uid=$(id -u) gid=$(id -g) docker-compose build


Start compose
$ uid=$(id -u) gid=$(id -g) docker-compose up


Connect to the container
$ uid=$(id -u) gid=$(id -g) docker exec -ti exchangerates_app_1 bash


Load fixtures from file (in container)
# concierge/manage.py loaddata --format=json exchange_rates/fixtures/init_data_currency.json


Collect staticfiles
# exchange_rates/manage.py collectstatic --noinput


Create super user
# exchange_rates/manage.py createsuperuser


Apply migrations
# exchange_rates/manage.py migrate

Run tests
# exchange_rates/manage.py test --keepdb
