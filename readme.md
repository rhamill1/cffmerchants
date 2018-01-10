##### Environment start up instructions
```
$ virtualenv venv
$ venv/bin/activate
$ pip install Flask
$ pip install gunicorn
$ pip freeze > requirements.txt
```
##### Deactivate Virtualenv
```
deactivate
```
##### Run Dev Server
```
$ export FLASK_APP=cffmerchants.py
$ export FLASK_DEBUG=1
$ python -m flask run
```
##### Deploy to Heroku
```

```
