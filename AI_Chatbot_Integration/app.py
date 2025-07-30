from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Use your valid Gemini API Key (from makersuite.google.com)
genai.configure(api_key="AIzaSyB2uiFnSIce9rNYzPRQeDhES4wwYF6U-cc")

# ✅ Correct model name for text input
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_response', methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
