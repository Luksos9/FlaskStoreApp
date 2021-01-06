from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') # it is a list of item models ( because store may contain many items)
#lazy is dynamic - dzieki temu self.items is no longer a list of items, it is a query builder with ability to look into the items table
#when we use .all() after self.items it allows us to get items from the table ( this lazy and all is done for performance purposes, so object is not created each time)
#dzieki temu creowanie jest szybsze, ale gdy uzywamy metody json to ten proces jest wolniejszy bo musi zagladac do tabeli
    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}  # dzieki temu zwracamy jsonowa reprezentacje obiektu tej klasy

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # Its query - SELECT * FROM items WHERE name = name | .first - zwraca tylko pierwszy tak jakby LIMIT 1

    def save_to_db(self): # insert + update
        db.session.add(self) # session - it is a collection of objects that we add to database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()