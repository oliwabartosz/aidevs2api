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
    app.run(debug=os.getenv("DEBUG"))
    # api_key = os.getenv("API_KEY")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
