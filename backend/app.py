from flask import Flask
from routes.chatbot_routes import chatbot_bp
from routes.convidado_routes import convidado_bp
from routes.lembrete_routes import lembrete_bp

app = Flask(__name__)
app.register_blueprint(chatbot_bp)
app.register_blueprint(convidado_bp)
app.register_blueprint(lembrete_bp)

# criar tabelas
from models import Base
from database import engine
Base.metadata.create_all(bind=engine)

if __name__=="__main__":
    app.run(debug=True)
