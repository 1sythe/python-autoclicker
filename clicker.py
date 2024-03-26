import time
import threading
from pynput.mouse import Button, Controller


def uitestlog(msg):
    print(f"[UI TEST MODE] {msg}")


class Clicker(threading.Thread):
    def __init__(self, interval, mouse):
        print("[DEBUG] AC Initialized")
        threading.Thread.__init__(self)
        self.interval = interval
        self.mouse = mouse
        self.button = Button.left
        self.running = False

    def click(self):
        self.running = True
        uitestlog("AC would start now")
        uitestlog(f"[Stats] Interval: {str(self.interval)}s ({1 / self.interval} CPS) | {str(self.button)}")
        #while self.running:
        #    self.mouse.click(self.button)
        #    time.sleep(self.interval)

        # This is only for UI testing purposes
        while self.running:
            uitestlog("Click")
            time.sleep(self.interval)

        uitestlog("AC would stop now")

    def stop(self):
        self.running = False


if __name__ == "__main__":
    clicker = Clicker(0.1, Controller())
    clicker.start()

    print("Clicking in 5 sec")
    time.sleep(5)

    clicker.click()
    time.sleep(5)
    clicker.stop()

