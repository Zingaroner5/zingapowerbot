import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import openai

app = FastAPI()

# Configura la chiave API di OpenAI
openai.api_key = 'RtaETJ8ZxI_2lwMigjAuQSrnpbj9cLaSLD0veN0FK4T3Blb'  # Rimuovi eventuali simboli extra come ">" alla fine

# Configura i template HTML
templates = Jinja2Templates(directory="templates")

# Simuliamo un "database" di utenti e canali
users_db = {
    "1": {"name": "Alessandro", "age": 45, "messages": []},
    "2": {"name": "Rita", "age": 30, "messages": []}
}

channels_db = {
    "1": {"name": "Notizie", "description": "Ultime notizie locali"},
    "2": {"name": "Sport", "description": "Discussioni su eventi sportivi"}
}

# Modello per il messaggio del chatbot
class ChatMessage(BaseModel):
    message: str

# Modello per i canali
class Channel(BaseModel):
    name: str
    description: str

# Endpoint per ottenere la lista dei canali
@app.get("/channels")
async def get_channels():
    return channels_db

# Endpoint per creare un nuovo canale
@app.post("/channels")
async def create_channel(channel: Channel):
    channel_id = str(len(channels_db) + 1)
    channels_db[channel_id] = {"name": channel.name, "description": channel.description}
    return {"message": "Canale creato con successo!", "channel_id": channel_id}

# Endpoint per il chatbot
@app.post("/chatbot/")
async def chatbot_response(user_message: ChatMessage):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message.message}]
    )
    return {"response": response['choices'][0]['message']['content']}

# Endpoint principale per il template HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Configura la porta per Heroku
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
