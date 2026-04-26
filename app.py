import os
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from groq import Groq

app = Flask(__name__)

# ── Groq Client ──────────────────────────────────────────
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set!")
client = Groq(api_key=api_key)
# ── Available Models ─────────────────────────────────────
MODELS = {
    "llama-3.3-70b-versatile": "Llama 3.3 70B (Best)",
    "llama-3.1-8b-instant":    "Llama 3.1 8B (Fast)",
    "mixtral-8x7b-32768":      "Mixtral 8x7B (Smart)",
    "gemma2-9b-it":            "Gemma2 9B (Google)",
}

DEFAULT_MODEL = "llama-3.3-70b-versatile"

# ── Routes ───────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", models=MODELS, default_model=DEFAULT_MODEL)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])
    model = data.get("model", DEFAULT_MODEL)

    if model not in MODELS:
        model = DEFAULT_MODEL

    system = {
        "role": "system",
        "content": (
            "You are a helpful, friendly AI assistant. "
            "Answer in the same language the user uses. "
            "Be concise but thorough."
        )
    }

    def generate():
        try:
            stream = client.chat.completions.create(
                model=model,
                messages=[system] + messages,
                stream=True,
                max_tokens=2048,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta
        except Exception as e:
            yield f"[Error: {str(e)}]"

    return Response(stream_with_context(generate()), content_type="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
