import json

from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

load_dotenv()
app = Flask(__name__)


@app.route('/send_question', methods=['POST'])
def post_question():
    try:
        data = request.get_json()
        if data:
            # Save the data to a file
            with open('messages.txt', 'w') as file:
                file.write(str(data) + '\n')

            return jsonify({'message': 'Data saved successfully'}), 200
        else:
            return jsonify({'error': 'No data provided'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_question')
def get_question():
    try:
        with open('messages.txt', 'r') as file:
            messages = [json.loads(line) for line in file.readlines()]

        return jsonify({'question': messages}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", False)

    app.run(host=host, port=port, debug=debug)