from flask import Blueprint, request, jsonify
from models import Convidado
from database import SessionLocal

convidado_bp = Blueprint("convidado", __name__)

@convidado_bp.route("/convidado", methods=["POST"])
def novo_convidado():
    dados = request.json
    nome = dados["nome"]
    email = dados["email"]
    acompanhantes = dados.get("acompanhantes", 0)

    db = SessionLocal()
    convidado = Convidado(nome=nome, email=email, acompanhantes=acompanhantes)
    db.add(convidado)
    db.commit()
    db.close()

    return jsonify({"status": "criado", "email": email})


@convidado_bp.route("/convidado/confirma", methods=["POST"])
def confirma_convidado():
    dados = request.json
    email = dados["email"]
    confirm = dados["confirmado"]

    db = SessionLocal()
    convidado = db.query(Convidado).filter_by(email=email).first()
    if not convidado:
        return jsonify({"erro": "não encontrado"}), 404

    convidado.confirmado = confirm
    db.commit()
    db.close()
    return jsonify({"status": "atualizado", "confirmado": confirm})
