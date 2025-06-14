import sqlite3

DB_PATH = "Pimenta.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_convidados():
    conn = get_connection()
    convidados = conn.execute("SELECT * FROM convidados").fetchall()
    conn.close()
    return [dict(row) for row in convidados]

def insert_convidado(data):
    conn = get_connection()
    conn.execute(
        "INSERT INTO convidados (nome, email, confirmado, acompanhantes, comentarios) VALUES (?, ?, ?, ?, ?)",
        (data["nome"], data["email"], data["confirmado"], data["acompanhantes"], data["comentarios"])
    )
    conn.commit()
    conn.close()
    