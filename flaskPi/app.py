from flask import Flask, jsonify , request , abort

app = Flask(__name__)

outlets = [
    {
        'id':1,
        'name': u'Bedroom',
        'currentStatus': u'ON',
        'timer': u'10:00',
        'timerStatus': u'ON'
    },
    {
        'id':2,
        'name': u'Nexus Player',
        'currentStatus': u'ON',
        'timer': u'10:00',
        'timerStatus': u'ON'
    },
    {
        'id':3,
        'name': u'Default 3',
        'currentStatus': u'ON',
        'timer': u'10:00',
        'timerStatus': u'ON'
    }
]


@app.route('/api/v1/wifiOutlets', methods=['GET'])
def get_outlets():
    return jsonify({'outlets': outlets})

@app.route('/api/v1/wifiOutlets/<int:outlet_id>', methods=['GET'])
def get_outlet(outlet_id):
    for outlet in outlets:
        if outlet['id'] == outlet_id:
            return jsonify({'outlet' : outlet})

@app.route('/todo/api/v1/updateWifiOutlet/<int:outlet_id>', methods=['PUT'])
def update_outlet(outlet_id):
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'currentStatus' in request.json and type(request.json['currentStatus']) is not unicode:
        abort(400)
    if 'timer' in request.json and type(request.json['timer']) is not unicode:
        abort(400)
    if 'timerStatus' in request.json and type(request.json['timerStatus']) is not unicode:
        abort(400)
    for outlet in outlets:
        if outlet['id'] == outlet_id:
            outlet['name'] = request.json.get('name', outlet['name'])
            outlet['currentStatus'] = request.json.get('currentStatus', outlet['currentStatus'])
            outlet['timer'] = request.json.get('timer', outlet['timer'])
            outlet['timerStatus'] = request.json.get('timer', outlet['timerStatus'])
            return jsonify({'outlet': outlet[0]})



@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
