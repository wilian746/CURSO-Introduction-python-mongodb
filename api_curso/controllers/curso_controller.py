import json
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId

from api_curso.databases.mongodb import MongoDB


def get_db():
    return MongoDB.get_instance().get_collection('sample')


def get_one(curso_id):
    try:
        return json.loads(dumps(get_db().find_one({"_id": ObjectId(curso_id)})))
    except InvalidId:
        return None

def get_all():
    return [json.loads(dumps(item)) for item in get_db().find({})]
    

def insert(curso):
    return json.loads(dumps(get_db().insert(curso)))


def update(curso_id, curso):
    try:
        return json.loads(
            dumps(get_db().update({"_id": ObjectId(curso_id)}, curso))
        )
    except InvalidID:
        return None


def delete(curso_id):
    try:
        return json.loads(
            dumps(get_db().remove({"_id": ObjectId(curso_id)}))
        )
    except InvalidId:
        return None