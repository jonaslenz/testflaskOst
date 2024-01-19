# hello.py

import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Worldfrom flask1!"


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
    return flask.jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(flask.request.get_json())
    return '', 204

if __name__ == "__main__":
    app.run()
