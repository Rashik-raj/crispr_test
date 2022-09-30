# How to run??
- Create virtualenv `python -m venv env`
- Activate virtualenv, for linux `source env/bin/activate` or for windows `env\Scripts\activate`
- Install requirements `pip install -r requirements.txt`
- Create **_.env_** file and add env variables as per **_example.env_** file
- Run Django server `python manage.py runserver`
- To view api docs
  - for [redoc](http://127.0.0.1:8000/api/docs/redoc)
  - for [swagger](http://127.0.0.1:8000/api/docs/swagger)

# How filters are being applied?
- For filtering in people api, I am using django-filter package
- For filtering in address api, I am writing my own logic to filter the data with _**__icontains**_

# Admin Credentials
- username: **admin**
- password: **admin**