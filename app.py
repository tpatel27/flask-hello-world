from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/plate1')
def hello_world():
    return jsonify(
        {
            "message": "success",
            "plate_text": "284FH8",
            "status": True,
        }
    )


@app.route('/api/plate2')
def hello_world():
    return jsonify(
        {
            "message": "success",
            "plate_text": "MRSNOOPY",
            "status": True,
        }
    )


@app.route('/api/plate3')
def hello_world():
    return jsonify(
        {
            "message": "success",
            "plate_text": "KL55R2473",
            "status": True,
        }
    )


@app.route('/api/plate4')
def hello_world():
    return jsonify(
        {
            "message": "success",
            "plate_text": "A5998",
            "status": True,
        }
    )