from flask import Flask, jsonify, request  # jsonify zmienia nasz slownik w string ktory przyjmuje JSON

# request - to co bylo przeslane w requescie (np. nazwa sklepu) chcemy otrzymac te dane

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99,
            }
        ]
    }
]  # lista przechowywuje sklepy, a slownik przechowywuje info o sklepie


# w info o sklepie sa items czyli lista przechowywujaca slownik z itemami takimi jak jego nazwa oraz cena


# POST = used to receive data
# GET = used to send data back only

# POST /store data: {name:} - tworzy nowy sklep z dana nazwa
@app.route('/store',
           methods=["POST"])  # domyslnie mamy GET wiec zmieniamy metode na POST by utworzyc za jej pomoca sklep
def create_store():
    request_data = request.get_json()  # dzieki tej linijce odczytujemy dane dzieki ktorym utworzymy nowy sklep (dane czyli np nazwe); TA METODA KONWERTUJE DO SLOWNIKA JSON (czyli stringa)
    new_store = {  # tworzymy nowy sklep
        'name': request_data['name'],
        # imie odczytujemy z requestu json, ktory bedzie juz slownikiem, bo zostal przekonwertowany wyzej
        'items': []
    }
    stores.append(new_store)  # dodajemy nowy sklep do sklepow
    return jsonify(
        new_store)  # musimy zwrocic jsonify nowego sklepu, bo inaczej zwracamy slownik (na nim pracowalismy), a musimy zawsze zwracac tekst


# GET /store/<string:name> - bierze sklep o danej nazwie i zwraca dane o nim
@app.route(
    '/store/<string:name>')  # to jest skladnia flaska 'name' tutaj wstawimy do funkcji get_store jako parametr i te 2 musza miec te sama nazwe np.http://127.0.0.1:5000/store/nazwa (czyli name)
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({
                       'message': 'store not found'})  # PAMIETAJ, zawsze zwracamy po jsonify (bo musimy konwertowac na string wszystko, a pracujemy na {} oraz ten slownik tworzyc


# GET /store - bierze liste wszystkich sklepów
@app.route('/store')
def get_stores():
    return jsonify({
        'stores': stores})  # dzieki temu stores variable, czyli zmienna przechowywujaca lista na gorze ze szczegolami sklepu zmieni sie w tekst, ktory JSON akceptuje (po to by bylo w powszednim jezyku)
    # stores to lista, a jesonify przyjmuje slownik wiec robimy z niej slownik gdzie lista stores to wartosc a 'stores' to klucz


# POST /store/<string:name>/item {name:, price:} - wklada wszystkie itemy do sklepu
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item - zwraca wszystkie itemy ze sklepu
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']}) # store['items'] to lista slownikow, wiec pamietaj zeby umiescic to tez jako wartosc dla klucza czyli {}
    return jsonify({'message': 'no store found'})


if __name__ == "__main__":
    app.run(port=5000)
