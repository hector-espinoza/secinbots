# Setup skeleton project 
```
heroku login
heroku create secinbots
git clone https://git.heroku.com/secinbots.git && cd secinbots
heroku git:remote -a secinbots
git checkout -b main
heroku repo:reset -a secinbots
echo "web: gunicorn secinbots.wsgi" > Procfile
echo "python-3.10.5" > runtime.txt
echo "django>=4.0, <5.0
    gunicorn
    django-heroku
    requests" > requirements.txt
git add .
git commit -m "Pushing Skeleton" 
git push heroku main
```

# Setup local python env
```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install django
```

# Setup django project
```
django-admin startproject secinbots
# remove top layer directory, copy paste secinbots manage.py to top secinbots folder
python manage.py startapp messagex
python manage.py migrate
```

# Setting superuser to check on users created
```
python manage.py createsuperuser
```

# Project/Server
```
python3 manage.py shell # get python shell on project
python3 manage.py runserver # run django server locally
python3 manage.py makemigrations # compile changes to models
python3 manage.py migrate # apply changes to models
```

# Users

## Create superuser
```
python3 manage.py createsuperuser
Username (leave blank to use 'hectorespinoza'): 
Email address: hectorjonathanespinoza@gmail.com
Password: test123
Password (again): test123
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Create a testing user1 and user2
```
python3 manage.py shell
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user(username="user1", first_name="Name1", last_name="Lastname1" email="user1@example.com", password="password1") # first_name and last_name are missing
>>> user.save()
>>> exit()
```

## Useful commands
```
- python3 manage.py check --deploy
- heroku run bash --remote origin (use this to update remote database by using python3 manage.py makemigrations then migrate)
- heroku addons:create papertrail
- python -m smtpd -n -c DebuggingServer localhost:1025
```

## TO-DOs
- remove debug setting on prod
- create fancy error page
- remove testing data from prod
- edit profile (or better ask for this on registration, at least Name, Lastname and valid email)
- move secrets to env vars:
    - https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project#step-3-creating-development-and-production-settings
- make it robust:
    - https://django-cryptography.readthedocs.io/en/latest/settings.html
- protect views from direct access