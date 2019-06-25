Usage
-----
Export environment for firebase server api key: 
```
SERVER_KEY='your-api-key'
```

Export google credentials environment:
```
GOOGLE_APPLICATION_CREDENTIALS='your-google-credentials-api-key'
```

Run web
-----------
```
docker-compose up --build
```

Migrate database
---------------
Access to docker container
```
docker-compose exec web bash
```

Migrate
```
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```

Start schedule worker
---------------------
Access to docker container
```
docker-compose exec web bash
```
Run worker
```
pipenv run python manage.py rqworker
piepnv run python manage.py rqscheduler
```