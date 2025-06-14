from .chatbot import responder_pergunta
from flask import Blueprint, request, jsonify
from models import ChatLog
from database import SessionLocal

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chatbot", methods=["POST"])
def chatbot():
    payload = request.json
    pergunta = payload.get("pergunta", "")
    email = payload.get("email")  # opcional identificação

    resposta = responder_pergunta(pergunta)

    # salvar no log
    db = SessionLocal()
    log = ChatLog(pergunta=pergunta, resposta=resposta, convidado_email=email)
    db.add(log)
    db.commit()
    db.close()

    return jsonify({"resposta": resposta})
