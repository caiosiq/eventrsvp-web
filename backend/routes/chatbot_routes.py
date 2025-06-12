from flask import Blueprint, request, jsonify
from chatbot import responder_pergunta

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chatbot", methods=["POST"])
def chatbot():
    pergunta = request.json.get("pergunta", "")
    resposta = responder_pergunta(pergunta)
    return jsonify({"resposta": resposta})
