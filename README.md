# KulierApi

Kulier Api (Simple Restful API) - Base Apistar ( python )

# Features Available

* **CRUD API**
* **BasicAuthentication**
* **Add User Authentication**
* **and others**

# Apistar Installation

    $ pip3 install apistar

Check Installation:

    $ apistar --version

# Installation

    $ clone this repository
    $ cd into that folder

Create a virtual environment

    $ python3 -m venv .venv

Execute to activate the virtual environment

    $ source .venv\bin\activate

Install the requirements

    $ pip3 install -r requirements.txt

# Create Tables


    $ apistar create_tables or python3 main.py create_tables

Run the API

    $ apistar run or python3 main.py run

Open your browser to <http://localhost:8080/docs> to access to site's interactive documentation

# How to Deploy

install gunicorn

    $ pip3 install gunicorn

run gunicorn

    $ gunicorn --bind 127.0.0.1:8000 main:app
