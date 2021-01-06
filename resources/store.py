from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    """Store only has a name so we will need get, post and delete endpoints (put method would change all about store, so it is better to just delete old and create new store"""

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "No store found"}, 404 # zwracamy tu tuple dict i kodu ktory flask importuje jako ze 1 to body a 2 czyli 404 to Status

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured while creating the store"}, 500 # 500 - internal server error (np w bazie danych)

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "store with name '{}' deleted".format(name)}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}