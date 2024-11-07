import tkinter as tk
from tkinter import messagebox
# Se hai un modello AI, importalo qui
# from ai_model import predict

def on_button_click():
    user_input = entry.get()
    # Qui puoi integrare la tua funzione AI
    # result = predict(user_input)
    result = f"Elaborazione di '{user_input}' completata."
    messagebox.showinfo("Risultato", result)

app = tk.Tk()
app.title("Super App AI")

label = tk.Label(app, text="Inserisci il tuo testo:")
label.pack(pady=10)

entry = tk.Entry(app, width=50)
entry.pack(pady=5)

button = tk.Button(app, text="Elabora", command=on_button_click)
button.pack(pady=20)

app.mainloop()

