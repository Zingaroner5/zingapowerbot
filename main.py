import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import openai

app = FastAPI()

# Configura la chiave API di OpenAI
openai.api_key = 'RtaETJ8ZxI_2lwMigjAuQSrnpbj9cLaSLD0veN0FK4T3Blb'  # Assicurati che la chiave sia corretta e completa

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
