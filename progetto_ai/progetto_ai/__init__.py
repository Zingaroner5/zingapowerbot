import random
import math
from datetime import datetime

def saluta():
    return "Ciao, sono il tuo progetto AI!"

def consiglia():
    consigli = ["Continua così!", "Non mollare!", "Credi in te stesso!", "Ogni passo è importante!"]
    return random.choice(consigli)

def somma(a, b):
    return a + b

# Nuova funzione per calcolo della radice quadrata
def calcola_radice(numero):
    return math.sqrt(numero)

# Nuova funzione per contare le parole
def conta_parole(frase):
    return len(frase.split())

# Nuova funzione per ottenere data e ora correnti
def data_ora_corrente():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
