from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)



# System instructions tell the AI how to behave before the user even types.
instructions = """
You are CTF-Buddy, an expert cybersecurity assistant. 
Your goal is to help the user solve CTF challenges (Web, Pwn, Reversing, Crypto, Forensics).
- Provide precise terminal commands (nmap, gobuster, sqlmap, etc.).
- When asked about vulnerabilities, explain the 'why' and then provide a 'PoC' (Proof of Concept).
- Keep responses concise and technical. 
- Use markdown for code blocks.
"""

genai.configure(api_key="AIzaSyDo253BQuodX1uLVmGWhznxWlV3TQ_jpKQ")


model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=instructions
)

#genai.configure(api_key="AIzaSyDo253BQuodX1uLVmGWhznxWlV3TQ_jpKQ")
#model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/')
def index():
    return render_template('test7.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)