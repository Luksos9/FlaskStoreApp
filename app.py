from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList # bez tego importu nie utworzy sie nam baza danych bo z resourcow importujemy Store resource, ktory importuje StoreModel ktory tworzy Store w bazie danych

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # mozna zmienic na postgre itp
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemy modyfication tracker is on but we are turning off the flask one
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)



