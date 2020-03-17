"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle,request,response,debug
import requests

# Base server
BASE_SERVER='https://huttoncourt.duckdns.org'

# Create the Bottle WSGI application.
app = Bottle()

# Define an handler for the root URL of our application.
@app.get('/<path:path>')
def reverse_get(path):
    """Redo the query to the host specified in the ipv6 param"""

    url = "{}/{}".format(BASE_SERVER, path)
    params = request.params
    headers = {"Content-Type": request.headers.get("Content-Type")}

    r = requests.get(url, headers=headers, params=params)

    response.status = int(r.status_code)
    return r.text

@app.post('/<path:path>')
def reverse_post(path):
    """Redo the query to the host specified in the ipv6 param"""

    url = "{}/{}".format(BASE_SERVER, path)
    params = request.params
    headers = {"Content-Type": request.headers.get("Content-Type")}
    data = request.body.getvalue()

    r = requests.post(url, headers=headers, params=params, data=data)

    response.status = int(r.status_code)
    return r.text

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
