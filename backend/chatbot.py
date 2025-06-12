from datetime import datetime
chat_log = []
def responder_pergunta(pergunta):
    pergunta = pergunta.lower()

    wedding_info = {
        "data": "12 de outubro de 2025",
        "local": "Espaço Villa Verde, São Paulo",
        "horario": "17h",
        "traje": "Esporte fino",
        "acompanhantes": "Permitido 1 por convidado",
        "presentes": "Lista disponível no site",
    }

    if "hora" in pergunta or "quando" in pergunta:
        resposta = f"O casamento será dia {wedding_info['data']} às {wedding_info['horario']}."
    elif "onde" in pergunta or "local" in pergunta:
        resposta = f"O local será {wedding_info['local']}."
    elif "traje" in pergunta:
        resposta = f"O traje recomendado é {wedding_info['traje']}."
    elif "acompanhante" in pergunta:
        resposta = wedding_info["acompanhantes"]
    elif "presente" in pergunta:
        resposta = wedding_info["presentes"]
    else:
        resposta = "Desculpe, não entendi. Pode perguntar de outra forma?"
    chat_log.append({
        "pergunta": pergunta,
        "resposta": resposta,
        "timestamp": datetime.now()
    })
    return resposta

