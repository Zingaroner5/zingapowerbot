# Database simulato per utenti
users_db = {}

# Funzione di registrazione
def registra_utente(username, password):
    if username in users_db:
        return "Nome utente già esistente!"
    else:
        users_db[username] = password
        return "Registrazione completata con successo!"

# Funzione di login
def login(username, password):
    if username in users_db and users_db[username] == password:
        return "Login effettuato!"
    else:
        return "Nome utente o password errati."

# Database di messaggi simulato
messages_db = {}

# Funzione per inviare un messaggio
def invia_messaggio(sender, recipient, message):
    if recipient not in messages_db:
        messages_db[recipient] = []
    messages_db[recipient].append((sender, message))
    return "Messaggio inviato!"

# Funzione per leggere i messaggi di un utente
def leggi_messaggi(username):
    if username in messages_db:
        return messages_db[username]
    else:
        return "Nessun messaggio."

# Esempio di utilizzo
print(registra_utente("utente1", "password123"))  # Registrazione
print(login("utente1", "password123"))            # Login
print(invia_messaggio("utente1", "utente2", "Ciao, come stai?"))  # Invia messaggio
print(leggi_messaggi("utente2"))                  # Leggi messaggi
