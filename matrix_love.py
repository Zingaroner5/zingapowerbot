import random
import time
import os

# Caratteri per l'effetto Matrix
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Funzione per l'effetto Matrix con "LOVE"
def matrix_effect():
    width = os.get_terminal_size().columns
    while True:
        # Alterna righe normali e righe con "LOVE"
        if random.random() < 0.1:  # Probabilità di mostrare "LOVE"
            print(" " * (width // 2 - 2) + "\033[31mLOVE\033[0m")  # Rosso per "LOVE"
        else:
            line = ''.join(random.choice(chars) for _ in range(width))
            print(f"\033[32m{line}\033[0m")  # Verde per Matrix
        time.sleep(0.1)

try:
    matrix_effect()
except KeyboardInterrupt:
    print("\nEffetto Matrix interrotto.")
