# unreduce

This website show the initial URL of short URL generated by URL shortening.

## Tech

For this branch, the website work with **flask**, a micro web-framework for **Python**.

I followed this [tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) to make this project.

## Setup

### Virtual environment

    python3 -m venv venv
    . venv/bin/activate
    pip install Flask

*In development mode.*

  . venv/bin/activate
    export FLASK_APP=unreduce
    export FLASK_ENV=development
    flask run

## Requirements

 - requests
 - flask
