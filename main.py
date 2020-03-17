"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle,request,response,debug
import requests

# Create the Bottle WSGI application.
app = Bottle()
debug(True)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


# Define an handler for the root URL of our application.
@app.get('/')
def ifttt_get():
    """Redo the query to the host specified in the ipv6 param"""

    params = request.params
    param_ipv6 = params.get("ipv6")
    del(params["ipv6"])

    headers = {"Content-Type": request.headers.get("Content-Type")}

    r = requests.get(param_ipv6, headers=headers, params=params)

    response.status = int(r.status_code)
    return r.text

@app.post('/')
def ifttt_post():
    """Redo the query to the host specified in the ipv6 param"""
    params = request.params
    param_ipv6 = params.get("ipv6")
    del(params["ipv6"])

    headers = {"Content-Type": request.headers.get("Content-Type")}
    data = request.body.getvalue()

    r = requests.post(param_ipv6, headers=headers, params=params, data=data)

    response.status = int(r.status_code)
    return r.text

# Define an handler for 404 errors.
@app.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
