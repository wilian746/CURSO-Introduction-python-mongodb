from tornado.web import RequestHandler
from api_curso.controllers import curso_controller
import json


class CursoHandler(RequestHandler):
    def get(self, curso_id):
        if curso_id:
            response = curso_controller.get_one(curso_id)
            if response:
                self.set_status(200)
                self.write(json.dumps(response))
            else:
                self.set_status(404)
                self.finish()
        else:
            response = curso_controller.get_all()
            if response:
                self.set_status(200)
                self.write(json.dumps(response))
            else:
                self.set_status(404)
                self.finish()


    def post(self, *args):
        body = self.request.body.decode()
        response = curso_controller.insert(json.loads(body))
        if response:
            self.set_status(200)
            self.write(json.dumps(response))
        else:
            self.set_status(404)
        
    
    def put(self, curso_id):
        body = self.request.body.decode()
        response = curso_controller.update(curso_id, json.loads(body))
        if response:
            self.set_status(200)
            self.write(json.dumps(response))
        else:
            self.set_status(404)
            self.finish()
        
    
    def delete(self, curso_id):
        response = curso_controller.delete(curso_id)
        if response:
            self.set_status(200)
            self.write(json.dumps(response))
        else:
            self.set_status(404)
            self.finish()