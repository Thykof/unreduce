from bottle import Bottle, run, template, request, static_file
import requests

app = Bottle()

@app.route('/')
def route():
    return template('route')

@app.post('/')
def url():
    error = None
    urls = list()
    url = request.forms.get('url')
    try:
        r = requests.get(url)
    except:
        error = "Invalid URL."
        return template('result', urls=urls, error=error)
    if r.status_code == 200:
        for elt in r.history:
            urls.append(elt.url)
        urls.append(r.url)
        return template('result', urls=urls, error=error)
    else:
        error = "The request failed."
        return template('result', urls=urls, error=error)

@app.route('/style.css')
def style():
    return static_file('style.css', root='static')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
