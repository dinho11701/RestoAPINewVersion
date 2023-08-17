from flask import Flask, jsonify
from flask import abort,make_response,request

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


api = Flask(__name__)

clients = [
    {
        'num' : 4389295968,
        'nom': u'Gogo',
        'prenom' : u'Gaga'
    },

    {
        'num' : 4389009804,
        'nom': u'Poto',
        'prenom' : u'Part'
    }
]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#return client's data on json
@api.route('/todo/api/v1.0/client', methods=['GET'])
def get_client():
    return jsonify({'client': clients})


@api.route('/todo/api/v1.0/client/<int:num_tel>', methods=['GET'])
def get_client_num(num_tel):
    client = [client for client in clients if client['num'] == num_tel]
    if len(client) == 0:
        abort(404)
    return jsonify({'client': client[0]})


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@api.route('/todo/api/v1.0/client', methods=['POST'])
def create_client():
    if not request.json or not 'num' in request.json:
        abort(400)
    client = {
        'num': clients[-1]['num'] + 1,
        'nom': request.json['nom'],
        'prenom': request.json.get('prenom', "")
    }
    clients.append(client)
    return jsonify({'client': client}), 201

@api.route('/todo/api/v1.0/client/<int:num>', methods=['PUT'])
def update_client(num):
    client = next((c for c in clients if c['num'] == num), None)
    if client is None:
        abort(404)  # Si le client n'est pas trouvé, renvoyer une réponse 404

    if not request.json:
        abort(400)  # Si la requête JSON est absente, renvoyer une réponse 400

    if 'prenom' in request.json:
        client['prenom'] = request.json['prenom']

    if 'nom' in request.json:
        client['nom'] = request.json['nom']

    return jsonify({'client': client})

#curl -X DELETE http://localhost:5000/todo/api/v1.0/client/4389009804
@api.route('/todo/api/v1.0/client/<int:num>', methods=['DELETE'])
def delete_task(num):
    client1 = [client1 for client1 in clients if client1['num'] == num]
    if len(client1) == 0:
        abort(404)
    clients.remove(client1[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    print_hi('PyCharm')
    api.run(debug=True)
