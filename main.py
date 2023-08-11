from flask import Flask, jsonify
from flask import abort

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


if __name__ == '__main__':
    print_hi('PyCharm')
    api.run(debug=True)