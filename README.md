# Project Management

## Setup

- Create virtual environment using

- Activate the envirnoment

- Install local and base requeriements using

```
pip install -r requirements/base.txt
```

```
pip install -r requirements/local.txt
```

- Run migrations

```
python manage.py makemigrations
```

```
python manage.py migrate --run-syncdb
```

- Start the server
```
python manage.py runserver
```

## admin credentials:

username: ruthvik
email: ruth@email.com
password: 123

- other user registration is possible by just signing up in signup page.

## database:

- postgres database used for this project. Connected the postgres database with PgAdmin4. 
- Changes made to the database can be done through the vs code terminal or from the pgAdmin4.
- More information regarding postgres is in '.env-local' file.

## Applications inside the project:

- 2 apps used in this project, namely USER and POLLS.
- User for implementing registration forms.
- Polls for implementing for authenitcated users(after logging in).
- User cannot attend poll if he/she is not registered with the application.

## Pages

- This project has a dashboard Page, Lists of Poll Page, Creation of Poll page, Poll Details Page.
- Once the user has voted a particular pole, they cannot vote for the same poll again.


