from wsgiref.simple_server import make_server

def app(environ, respond):
	respond('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
	yield "Hello world!\n\nOK!... Let's do this one last time! (no cap fr fr this time maybe ;-)".encode('utf-8')

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()
