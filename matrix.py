import random
import time
import os

# Definisce i caratteri da utilizzare
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*"

# Imposta la dimensione dello schermo
width = os.get_terminal_size().columns

# Funzione per creare l'effetto Matrix
def matrix_effect():
    while True:
        # Genera una riga casuale di caratteri
        line = ''.join(random.choice(chars) for _ in range(width))
        print(f"\033[32m{line}\033[0m")  # Colore verde
        time.sleep(0.05)  # Velocità dell'effetto

try:
    matrix_effect()
except KeyboardInterrupt:
    print("\nEffetto Matrix interrotto.")
