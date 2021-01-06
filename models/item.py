from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel') # dzieki SQL Alchey mozemy zamiast jointu po prostu podac ze store

    def __init__(self, name, price, store_id):#dzieki store_id mozemy sie upewnic ze dla okreslonego item modelu ktry tworzymy, ma przypisana wartosc sklepu do bazy danych ( kazdy item musi nalezec do jakiegos sklepu)
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}  # dzieki temu zwracamy jsonowa reprezentacje obiektu tej klasy

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # Its query - SELECT * FROM items WHERE name = name | .first - zwraca tylko pierwszy tak jakby LIMIT 1

    def save_to_db(self): # insert + update
        db.session.add(self) # session - it is a collection of objects that we add to database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()