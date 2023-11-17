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
            with open('messages.txt', 'w') as file:
                json.dump(data, file)
                file.write('\n')  # Add a newline after each JSON object

            return jsonify({'message': 'Data saved successfully'}), 200
        else:
            return jsonify({'error': 'No data provided'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_question')
def get_messages():
    try:
        messages = []
        with open('messages.txt', 'r') as file:
            for line in file:
                # Parse each line as JSON and directly append to messages list
                message = json.loads(line)
                messages.append(message)

        return jsonify(messages=messages), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500




if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", False)

    app.run(host=host, port=port, debug=debug)