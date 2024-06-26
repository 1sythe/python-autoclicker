import time
import threading
import sqlite3

from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController, KeyCode


def uitestlog(msg):
    print(f"[UI TEST MODE] {msg}")


class Clicker(threading.Thread):
    def __init__(self, interval, mouse):
        print("[DEBUG] AC Initialized")
        threading.Thread.__init__(self)
        self.interval = interval
        self.mouse = mouse
        self.running = False

        # 0 = Mouse; 1 = Keyboard
        self.mode = 0

        self.mouse_key = Button.left
        self.keyboard_key = Key.space

        self.start_key = Key.f1
        self.stop_key = Key.f2

        self.load_config()

    def load_config(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS config (
                            id INTEGER PRIMARY KEY,
                            mode INTEGER,
                            mouse_button TEXT,
                            keyboard_key TEXT,
                            start_key TEXT,
                            stop_key TEXT)''')

        # Fetch config from the database
        cursor.execute("SELECT * FROM config WHERE id = 1")
        row = cursor.fetchone()
        if row:
            self.mouse_key = getattr(Button, row[2]) if row[2] else Button.left
            #self.start_key = getattr(Key, row[4]) if row[4] else Key.f1 and hasattr(, row[4])
            try:
                self.keyboard_key = getattr(Key, row[3])
            except:
                self.keyboard_key = f'{row[3]}'
            try:
                self.start_key = getattr(Key, row[4])
            except:
                self.start_key = f'{row[4]}'
            try:
                self.stop_key = getattr(Key, row[5])
            except:
                self.stop_key = f'{row[5]}'


        conn.commit()
        conn.close()

    def save_config(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        # Convert Key object to string representation if available
        keyboard_key_name = self.keyboard_key.name if hasattr(self.keyboard_key, 'name') else str(self.keyboard_key)
        start_key_name = self.start_key.name if hasattr(self.start_key, 'name') else str(self.start_key)
        stop_key_name = self.stop_key.name if hasattr(self.stop_key, 'name') else str(self.stop_key)

        # Save config to the database
        cursor.execute(
            "REPLACE INTO config (id, mouse_button, keyboard_key, start_key, stop_key) VALUES (?, ?, ?, ?, ?)",
            (1, self.mouse_key.name, keyboard_key_name, start_key_name, stop_key_name))

        conn.commit()
        conn.close()

    def update_mouse_button(self, new_button):
        self.mouse_key = new_button
        self.save_config()

    def update_keyboard_key(self, new_key):
        self.keyboard_key = new_key
        self.save_config()

    def update_start_key(self, new_start_key):
        self.start_key = new_start_key
        self.save_config()

    def update_stop_key(self, new_stop_key):
        self.stop_key = new_stop_key
        self.save_config()

    def click(self, start_delay=0):
        self.running = True
        uitestlog("AC would start now")
        uitestlog(
            f"[Stats] Interval: {str(self.interval)}s | Mode: {'Mouse' if self.mode == 0 else 'Keyboard'} | Mouse Button: {str(self.mouse_key)} | Keyboard Key: {str(self.keyboard_key)}")

        if start_delay > 0:
            uitestlog(f"Starting in {start_delay} seconds")
            time.sleep(start_delay)

        while self.running:
            if self.mode == 0:  # Mouse mode
                #self.mouse.click(self.mouse_key)
                print("Clicked ", self.mouse_key)

            else:  # Keyboard mode
                #with KeyboardController().pressed(self.keyboard_key):
                #    pass
                print("Pressed ", self.keyboard_key)

            time.sleep(self.interval)

    def stop(self):
        self.running = False
        self.save_config()


if __name__ == "__main__":
    clicker = Clicker(0.1, Controller())

    clicker.mode = 0
    threading.Thread(target=clicker.click).start()
    time.sleep(5)
    clicker.stop()

    clicker.mode = 1
    threading.Thread(target=clicker.click).start()
    time.sleep(5)
    clicker.stop()

