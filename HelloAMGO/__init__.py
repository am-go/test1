from flask import Flask
application = Flask(__name__)
application.debug = True

from HelloAMGO.view import *
from HelloAMGO.session import *
from HelloAMGO.joining import *
from HelloAMGO.app.dbModule import *
from HelloAMGO.table import *


'''
# response_class
custom_res = Response("Custom Response", 200, {'test': 'ttt'})
return make_response(custom_res)
# str : Simple String (HTML, JSON)
return make_response("custom response")

# WSGI(WebServer Gateway Interface)
@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'), 
					('Content-Length', str(len(body))) ]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)
'''

