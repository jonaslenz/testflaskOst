# hello.py

import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World from flask 5001!"


incomes = [
    { 'description': 'salary',
      'amount': 5001 }
]


@app.route('/incomes')
def get_incomes():
    return flask.jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(flask.request.get_json())
    return '', 204

if __name__ == "__main__":
    app.run(port=5001)
