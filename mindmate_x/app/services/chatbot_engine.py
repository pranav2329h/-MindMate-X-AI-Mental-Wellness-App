from dotenv import load_dotenv
import os
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_reply(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a kind and supportive mental health assistant."},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=100
        )
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        return f"Error: {str(e)}"
