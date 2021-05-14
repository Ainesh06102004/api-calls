from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [{'id': 1, 'title': u"eating",
          'description': u"very hungry, haven't eaten since lunch", 'status': False},
         {'id': 2, 'title': u"sleeping",
          'description': u"very sleepy too, haven't slept since yesterday", 'status': False}]


@app.route("/")
def hello_world():
    return "Hello world!!!"


@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({'status': "error", 'message': "Please provide data"}, 400)

    task = {'id': tasks[-1]['id'] + 1, 'title': request.json['title'],
            'description': request.json.get('description', " "), 'status': False}
    
    tasks.append(task)

    return jsonify({'status': "successful", 'message': "Task Added successfully"})

@app.route("/get-data")
def get_task():
    return jsonify({"data": tasks})

if __name__ == '__main__':
    app.run(debug=True)
