import os
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from groq import Groq

app = Flask(__name__)

# ── Groq Client ──────────────────────────────────────────
api_key = os.environ.get("GROQ_API_KEY", "").strip()
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set in environment variables!")

client = Groq(api_key=api_key)

# ── Available Models ─────────────────────────────────────
MODELS = {
    "llama-3.3-70b-versatile": "Llama 3.3 70B (Best)",
    "llama-3.1-8b-instant":    "Llama 3.1 8B (Fast)",
    "mixtral-8x7b-32768":      "Mixtral 8x7B (Smart)",
    "gemma2-9b-it":            "Gemma2 9B (Google)",
}

DEFAULT_MODEL = "llama-3.3-70b-versatile"

# ── CORS Helper ───────────────────────────────────────────
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"]  = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

# ── Routes ───────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", models=MODELS, default_model=DEFAULT_MODEL)

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return add_cors(jsonify({"ok": True}))

    try:
        data     = request.get_json(force=True)
        messages = data.get("messages", [])
        model    = data.get("model", DEFAULT_MODEL)

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

        resp = Response(stream_with_context(generate()), content_type="text/plain; charset=utf-8")
        return add_cors(resp)

    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.status_code = 500
        return add_cors(resp)

@app.route("/health")
def health():
    return add_cors(jsonify({"status": "ok", "models": list(MODELS.keys())}))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)