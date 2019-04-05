
```bash
$ python -m venv env
$ source env/bin/activate
(env) $ pip install flask
(env) $ pip install gunicorn
(env) $ pip install line-bot-sdk
(env) $ pip install google-api-python-client
(env) $ pip install google-auth-httplib2
(env) $ pip install google-auth-oauthlib

(env) $ echo Python 3.7.2 >runtime.txt
(env) $ pip freeze > requirements.txt
(env) $ echo web: gunicorn app:app --log-file=- > Procfile
(env) $ touch server.py
```