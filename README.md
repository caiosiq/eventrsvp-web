O objetivo é oferecer uma plataforma bonita, funcional e inteligente para informar os convidados, permitir confirmações de presença (RSVP), exibir fotos e enviar mensagens aos noivos. O projeto também será usado para aprendizado prático em frontend, backend, banco de dados e inteligência artificial.


## 📁 Estrutura do Projeto
/backend
├── app.py                   # Arquivo principal do servidor Flask
├── chatbot.py               # Código da IA com respostas
├── routes/
│   └── chatbot_routes.py    # Rota da API do chatbot
├── static/                  # (opcional) arquivos estáticos se precisar
├── templates/               # (opcional) HTML se quiser testar direto
└── requirements.txt         # Lista de bibliotecas Python necessárias


### 📡 Endpoints da API

#### POST /chatbot
Recebe uma pergunta e retorna uma resposta textual.

##### Body:
```json
{ "pergunta": "Onde é o casamento?" }
```
##### Response:
```json
{ "resposta": "O casamento será no Espaço Villa Verde, São Paulo." }
```
## 🧠 Visão da IA e Integração com Banco de Dados

Atualmente, a rota `/chatbot` responde perguntas usando regras simples baseadas em palavras-chave.

### 📌 Futuros aprimoramentos planejados:

- Substituição do sistema atual por uma IA mais avançada (ex: usando embeddings, LangChain ou API da OpenAI).
- Acesso direto ao banco de dados para:
  - Verificar presença de convidados
  - Personalizar respostas de acordo com o nome/email
  - Confirmar quantidade de acompanhantes
- Criação de logs de perguntas e respostas para análise e melhorias futuras.

Esses dados poderão ser usados tanto pela IA simples atual quanto pela futura IA mais poderosa.