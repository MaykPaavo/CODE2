# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from wsgiref.simple_server import make_server

def app(environ, respond):
	respond('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
	yield "Hello w€rld😞!".encode('utf-8')

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()
