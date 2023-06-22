#! /bin/bash

# build image
#docker compose -f docker-compose.yml -f docker-compose.test.yml --project-name revapptest build

# run container and get exit code
#docker compose -f docker-compose.yml -f docker-compose.test.yml --project-name revapptest up --exit-code-from api --abort-on-container-exit
#exit_code=$?

# stop container
#docker compose -f docker-compose.yml -f docker-compose.test.yml --project-name revapptest down

# exit with container exit code
#exit $exit_code

# remove test database
#rm -rf ./test_db
