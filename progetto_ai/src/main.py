from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import random
import time

app = FastAPI()

class User(BaseModel):
    pin: str  # Solo il PIN è necessario

users_db = {}

# Simulazione riconoscimento facciale durante la registrazione
async def facial_recognition():
    print("Posiziona il viso davanti alla fotocamera per il riconoscimento...")
    return random.choice([True, False])

# Simulazione autenticazione con impronta digitale durante il login
async def fingerprint_auth():
    print("Posiziona il dito sul sensore di impronte digitali...")
    return random.choice([True, False])

@app.post("/register")
async def register(user: User):
    if user.pin in users_db:
        raise HTTPException(status_code=400, detail="Utente già registrato.")
    
    if not await facial_recognition():
        raise HTTPException(status_code=400, detail="Riconoscimento facciale fallito. Registrazione non riuscita.")
    
    users_db[user.pin] = {
        "registered_at": datetime.now(),
        "requires_fingerprint": True
    }
    return {"message": "Registrazione avvenuta con successo"}

@app.post("/login")
async def login(user: User):
    if user.pin not in users_db:
        raise HTTPException(status_code=400, detail="Utente non registrato.")
    
    if users_db[user.pin]["requires_fingerprint"]:
        if not await fingerprint_auth():
            raise HTTPException(status_code=400, detail="Autenticazione impronta digitale fallita. Accesso negato.")
        return {"message": "Accesso con impronta digitale avvenuto con successo"}
    
    raise HTTPException(status_code=400, detail="Errore durante l'accesso.")

@app.get("/status")
async def get_status(pin: str):
    if pin in users_db:
        method = "impronta digitale" if users_db[pin]["requires_fingerprint"] else "altro metodo"
        return {"status": f"L'utente {pin} deve usare {method} per accedere"}
    return {"status": "Utente non registrato"}

# Mock database per i canali con posizione (dati fittizi)
channels_db = [
    {"name": "Canale Sportivo", "lat": 41.9028, "lon": 12.4964},
    {"name": "Musica Locale", "lat": 45.4642, "lon": 9.1900},
    {"name": "Arte e Cultura", "lat": 40.8518, "lon": 14.2681}
]

class Location(BaseModel):
    lat: float
    lon: float

@app.post("/find_nearby_channels")
async def find_nearby_channels(location: Location) -> List[dict]:
    nearby_channels = []
    for channel in channels_db:
        distance = ((location.lat - channel["lat"]) ** 2 + (location.lon - channel["lon"]) ** 2) ** 0.5
        if distance < 0.5:  # raggio di 50 km
            nearby_channels.append(channel)

    if not nearby_channels:
        raise HTTPException(status_code=404, detail="Nessun canale vicino trovato.")
    
    return nearby_channels
