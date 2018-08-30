from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from unreduce.db import get_db

bp = Blueprint('home', __name__, url_prefix='/home')



@bp.route('/home', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        url = request.form['url']
        error = None

        if not url:
            error = 'URL is required.'
        elif url == "":
            error = 'URL is empty.'

        if error is None:
            db.execute('INSERT INTO req (url) VALUES (?)', (url))
            db.commit()
            return redirect(url_for('home.home'))

        flash(error)

    return render_template('auth/register.html')
