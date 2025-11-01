from wsgiref.simple_server import make_server
from flask import Flask, render_template, request

numero = 0

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    global numero
    print("*******")
    if(request.args['op']=="p"):
        numero = numero + int(request.args['num'])
    if(request.args['op']=="m"):
        numero = numero - int(request.args['num'])
    if(request.args['op']=="t"):
        numero = numero * int(request.args['num'])
    return render_template('vastaus.html', num=numero)

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()

#from wsgiref.simple_server import make_server
#
#def app(environ, respond):
#	respond('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
#	yield "Hello world!\n\nOK!... Let's do this one last time! (no cap fr fr this time maybe ;-)".encode('utf-8')

#if __name__ == '__main__':
#    with make_server("localhost", 8000, app) as server: 
#        server.serve_forever()
