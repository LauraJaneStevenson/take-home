To Do List
==========

Summary
-------

Web application that allows users to view, save, and edit goals they want to achieve.

About the Developer
-------------------

To Do List was created by Laura Stevenson. Learn more about her at [LinkedIn](https://www.linkedin.com/in/laura-stevenson-design)

Technologies
------------

#### Tech Stack
* Python
* Flask
* Jinja2
* SQLAlchemy
* HTML
* CSS
* Javascript
* JQuery
* Bootstrap


Setup/Installation
-----

#### Requirements:

* PostgresSQL
* Python 3.6

To run this app on your local computer, please follow these steps:

Clone repository:

```
$ git clone https://github.com/LauraJaneStevenson/take-home.git
```

Create a virtual environment:

```
$ virtualenv env
```

Activate the virtual environment: 

```
$ source env/bin/activate
```

Install dependencies:

```
$ pip3 install -r requirements.txt
```

Create database:

```
$ createdb todos
```

Create tables:

```
$ python3 -i model.py

>>> db.create_all()
```

Run app from command line:

```
$ python3 server.py
```


