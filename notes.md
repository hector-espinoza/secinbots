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
python manage.py startapp users
python manage.py migrate
```

# Setting superuser to check on users created
```
python manage.py createsuperuser
```