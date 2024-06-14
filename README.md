# Dockerized Authentication Service

A simple production-ready project to understand how authentication works. 

## Description

This loginapp can be readily setup on production server using docker. The app consists of three docker services - django, PostgreSQL and Nginx.

## Installation

Instructions for installing the project.
```bash
git clone https://github.com/harrypreeth/loginservice.git
cd loginservice
```

Add environment variable files for production to project root directory:
```bash
touch .env.prod
touch .env.prod.db
```
```bash
# .env.prod
DEBUG=0
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DB=user_db
SQL_USER=dbadmin
SQL_PASSWORD=dbadmin1234
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
```bash
# .env.prod.db
POSTGRES_USER=dbadmin
POSTGRES_PASSWORD=dbadmin1234
POSTGRES_DB=user_db
```

Update the file permissions locally:
```bash
chmod +x loginapp/entrypoint.prod.sh
``` 

Build new images and spin up the containers in detach-mode:
```docker
docker-compose -f docker-compose.prod.yaml up -d --build
``` 

Run the migrations:
```docker
docker-compose -f docker-compose.prod.yaml exec web python manage.py makemigration --noinput

docker-compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput
``` 

To create superuser:
```docker
docker-compose -f docker-compose.prod.yaml exec web python manage.py createsuperuser
```

To collect staticfiles:
```docker
docker-compose -f docker-compose.prod.yaml exec web python manage.py collectstatic
``` 

To connect to db service in interactive-mode:
```docker
docker-compose -f docker-compose.prod.yaml exec db psql --username=<username> --dbname=<db-name>
``` 

To check logs:
```docker
docker-compose -f docker-compose.prod.yaml logs -f
```

To check if the volume was created and running successfully:
```docker
docker volume inspect <volume-name>
```

To bring down the containers and volumes:
```docker
docker-compose -f docker-compose.prod.yaml down -v
``` 