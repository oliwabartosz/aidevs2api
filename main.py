from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/openapi', methods=['POST'])
def post_question():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    # Use Gunicorn for production
    host = '0.0.0.0'

    app.run(host=host, port=5000, debug=False)