from flask import Flask, request, jsonify
from nexus_ai import NexusAI

app = Flask(__name__)
nexus_ai = NexusAI(api_key="your_openai_api_key")

@app.route('/ask-socratic', methods=['POST'])
def ask_socratic():
    data = request.json
    answer = nexus_ai.ask_socratic(data['question'])
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
