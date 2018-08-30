import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def route():
    return render_template('route.html')

@app.route('/', methods=['POST'])
def url():
    url = request.form.['url']
    if url == '':
        return render_template('route.html')
    try:
        r = requests.get(url)
    except:
        error = "Invalid URL."
        return render_template('route.html', error=error)
    if r.status_code == 200:
        urls = list()
        for elt in r.history:
            urls.append(elt.url)
        urls.append(r.url)
        return render_template('route.html', urls=urls)
    else:
        error = "The request failed."
        return render_template('route.html', error=error)
