import tornado.web
import tornado.ioloop
from api_curso.handlers.curso_handler import CursoHandler

def make_app():
    return tornado.web.Application([
        (r'/(.*)', CursoHandler)
    ])
    

def run(port):
    print(port)
    make_app().listen(port)
    tornado.ioloop.IOLoop.current().start()
