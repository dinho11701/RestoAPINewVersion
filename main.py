from flask import Flask, jsonify
from flask import abort

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


api = Flask(__name__)

client = [
    {
        'num' : u'438-929-5968',
        'nom': u'Gogo',
        'prenom' : u'Gaga'
    },

    {
        'num' : u'438-900-9804',
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
    return jsonify({'client': client})

if __name__ == '__main__':
    print_hi('PyCharm')
    api.run(debug=True)