import requests

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from unreduce.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')



@bp.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        url = request.form['url']
        db = get_db()
        error = None
        urls = list()

        if not url:
            error = 'URL is required.'
        else:
            url = url.strip()
            if url == "":
                error = 'URL is empty.'

        if error is None:
            try:
                r = requests.get(url)
            except:
                error = "Invalid URL."
            else:
                if r.status_code == 200:
                    for elt in r.history:
                        urls.append(elt.url)
                    urls.append(r.url)
                else:
                    error = "The request failed."
            finally:
                result = None if len(urls) == 0 else urls[-1]
                db.execute('INSERT INTO req (url, result) VALUES (?, ?)', (url, result))
                db.commit()
        if error is not None:
            flash(error)
        return render_template('results.html', urls=urls, error=error)

    return render_template('home.html')


@bp.route('/db')
def show_res():
    db = get_db()
    reqs = db.execute('SELECT * FROM req').fetchall()
    print(reqs[1])
    return render_template('db.html', reqs=reqs)
