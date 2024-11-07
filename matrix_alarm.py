from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import random
import os

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
love_chars = "LOVE💓💖💞"

# Effetto Matrix
def generate_matrix_text(width):
    return ''.join(random.choice(chars) for _ in range(width))

class MatrixAlarmApp(App):
    def build(self):
        self.label = Label(text='', font_size='20sp', markup=True)
        Clock.schedule_interval(self.update_matrix, 0.1)
        self.sound = SoundLoader.load('alarm_sound.mp3')  # Aggiungi un suono d'allarme MP3
        return self.label

    def update_matrix(self, dt):
        width = self.label.width // 10
        matrix_text = generate_matrix_text(int(width))
        self.label.text = f"[color=00FF00]{matrix_text}[/color]"

    def on_touch_down(self, touch):
        if self.sound:
            self.sound.play()  # Fa partire l’allarme su tocco

    def stop_alarm(self):
        if self.sound:
            self.sound.stop()

# Esegui l'app
if __name__ == '__main__':
    MatrixAlarmApp().run()
