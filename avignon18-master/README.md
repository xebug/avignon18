# Femto tutorial

## Installing the environment

To make sure we have the right environment, we will use [*virtualenv*](https://virtualenv.pypa.io/en/latest/).

To prepare an virtualenv:

```bash
gullinbursti:avignon18 dsa$ virtualenv venv
New python executable in /Users/dsa/Documents/inria/Cours/Avignon/2018-2019/1e_semestre_2/projet/avignon18/venv/bin/python
Installing setuptools, pip, wheel...done.
gullinbursti:avignon18 dsa$
```

Then we go in our virtualenv:

```bash
gullinbursti:avignon18 dsa$ source venv/bin/activate
(venv) gullinbursti:avignon18 dsa$ 
```
Now, every Python tuning that we will do will not affect the rest of our system.

In this project we will use the [Flask](http://flask.pocoo.org) microframework to create the APIs needed in our project. See __src/server.py__ to see a basic functional system.

The best way to interact with our REST API is to use the [Requests](http://docs.python-requests.org/en/master/user/quickstart/) library. See __src/requests.py__

We put all dependencies in __src/requirements.txt__. To install them, we can just use _pip_ as usual:

```bash
(venv) gullinbursti:avignon18 dsa$ pip install -r src/requirements.txt 
```

Voila! Now you have anything you need for the project, have fun :)
