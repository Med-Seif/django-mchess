#!/bin/bash
CONTAINER_NAME='mchess_django' # see docker-compose.yml if you want to change this parameter

[ -z "$1" ] && echo "Please specify a valid django admin command" && exit

sudo docker exec -it $CONTAINER_NAME python manage.py "$@"

./bin/fixowns.sh
