from werkzeug.security import safe_str_cmp  # dzieki temu mozemy porównywac stringi w pewny sposób (unicode itp)
from models.user import UserModel  # importuje klase z uzytkownikami

# # Przechowywuje uzytkownikow w liscie, uzytkownicy to instancje klasy User
# users = [
#     User(1, 'bob', 'asdf')
# ]
#
# username_mapping = {u.username: u for u in
#                     users}  # czyli dla kazdego uzytkownika w liscie users dodajemy do username_mapping jego username (czyli User.username - username to atrybut)
#
# userid_mapping = {u.id: u for u in users}  # podobnie jak powyzej tylko teraz korzystamy z atrybutu id


def authenticate(username, password):
    user = UserModel.find_by_username(username)  # bierzemy ze slownika username, a gdy nie ma nadajemy mu None
    if user and safe_str_cmp(user.password, password):  # lepsza wersja porównywania stringów - bezpieczniejsza
        return user


def identity(payload):  # to dla JWT; to zawartosc dla JWT
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
