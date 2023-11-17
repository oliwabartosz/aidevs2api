import json
from time import sleep

from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
app = Flask(__name__)

llm = ChatOpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-4-1106-preview")
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            """You are a nice chatbot having a conversation with a human. Answer with one word"""
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)
# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name.
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

@app.route('/ownapi', methods=['POST'])
def post_question():
    sleep(5)
    data = request.get_json()
    print(data)
    reply = (conversation({"question": data["question"]})['text'])
    with open('conversation.txt', 'a') as file:
        file.write(str(data) + '\n' + reply + '\n')


    return jsonify({'reply': reply})


@app.route('/get_question')
def get_messages():
    try:
        with open('messages.txt', 'r') as file:
            # Read the first line as JSON
            message = json.loads(file.readline().strip())

        return jsonify(message), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", False)

    app.run(host=host, port=port, debug=debug)
