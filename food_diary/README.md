FOOD DIARY
=====

(IN PROGRESS)

A Django RESTful Application project using Docker
===


Description
====
This is simple Django project that uses Django REST framework.
Thanks to that application u can easy count your daily callories intake.
App is in the form of a diary with division into days and meals.

The user selects the products and the quantity consumed from the available database. If a given product is not in the database, he can add it himself.
There is also available API to enter product list into database.

Run
====

Build and run:
```
    docker-compose up -d --build
```

Recreate the DB
```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
```
