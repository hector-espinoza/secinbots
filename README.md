# CyberSecurity Specialization Capstone Project

## Live App URL
```
https://secinbots.herokuapp.com/index.html
```

## GitHub Repo URL
```
https://github.com/hector-espinoza/secinbots.git
```

## Local set up
```
gh repo clone hector-espinoza/secinbots
cd secinbots
python3 manage.py runserver # runs django server locally
```

## Notes
I strongly recommend using the Live App for testing and convenience, IF you still want to give it a try locally please take the following considerations:
1. You'll need [Postgress sever](https://www.postgresql.org/download/) running locally with a DB called `secinbots.v1`
2. You'll need SMTP server running locally. In a new terminal run `python -m smtpd -n -c DebuggingServer localhost:1025`
3. This project differenciate between Dev from Prod configs, check settings.py for local (Dev) ENV configs
4. There are known secret keys hardcoded on Dev settings, these are for you to change on your local instance. They're obviously different in Prod and rotated from time to time. (i.e. `SECRET_KEY`, `SECURED_FIELDS_KEY` and `SECURED_FIELDS_HASH_SALT`

