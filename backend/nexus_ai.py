import openai

class NexusAI:
    def __init__(self, api_key):
        openai.api_key = api_key

    def ask_socratic(self, question):
        prompt = f"Nexus AI Debugger: Consider the following problem: {question}. What could be its potential causes based on known principles of logic and reason?"
        response = openai.Completion.create(
            engine="davinci-codex", prompt=prompt, max_tokens=150
        )
        return response.choices[0].text.strip()
