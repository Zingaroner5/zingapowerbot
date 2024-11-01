import random
import time
import os

# Caratteri per l'effetto Matrix
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
love_chars = "LOVE💓💖💞"  # Lettere e cuori

# Funzione per effetto Matrix con LOVE e cuori
def matrix_love_fullscreen():
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    while True:
        for _ in range(height):
            line = ''.join(
                random.choice(love_chars if random.random() < 0.1 else chars) 
                for _ in range(width)
            )
            print(f"\033[32m{line}\033[0m")  # Verde per Matrix, con LOVE e cuori
        time.sleep(0.1)
        os.system('clear')  # Pulisce lo schermo per rinfrescare l'effetto

try:
    matrix_love_fullscreen()
except KeyboardInterrupt:
    print("\nEffetto Matrix LOVE interrotto.")
