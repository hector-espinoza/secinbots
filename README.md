# CyberSecurity Specialization Capstone Project

## Live App URL
```
https://secinbots.herokuapp.com/index.html
```

## GitHub Repo URL
```
https://github.com/hector-espinoza/secinbots.git
```

## Local setup
```
gh repo clone hector-espinoza/secinbots
cd secinbots
python3 manage.py runserver # runs django server locally
```

## Notes
1. You'll need [Postgress sever](https://www.postgresql.org/download/) running locally with a DB called `secinbots.v1`
2. You'll need SMTP server running locally. In a new terminal run `python -m smtpd -n -c DebuggingServer localhost:1025`
3. This project differenciate Dev from Prod configs, check settings.py for local (Dev) ENV configs

