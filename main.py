from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

load_dotenv()
app = Flask(__name__)


@app.route('/openapi', methods=['POST'])
def post_question():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    # Use Gunicorn for production
    host = '0.0.0.0'
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", False)

    app.run(host=host, port=port, debug=debug)