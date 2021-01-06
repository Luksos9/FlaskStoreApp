from db import db


class UserModel(db.Model):
    """user objects - zamiast slowników tworzymy objekty"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # id - to juz auto inkrementuje wiec nie musimy dawac w inicie bo juz jest generowane (username oraz password podajemy)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod  # bo uzywamy Clasy (cls)
    def find_by_username(cls, username):
        return cls.query.filter_by(
            username=username).first()  # ten sam kolor to parametr i argument, a na kolor pomarancz jest nazwa tabeli

    @classmethod  # bo uzywamy Clasy (cls)
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
