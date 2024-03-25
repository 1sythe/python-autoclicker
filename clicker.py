import time
import threading
from pynput.mouse import Button, Controller


class Clicker(threading.Thread):
    def __init__(self, interval, mouse):
        print("[DEBUG] AC Initialized")
        threading.Thread.__init__(self)
        self.interval = interval
        self.mouse = mouse
        self.button = Button.left
        self.running = False

    def run(self):
        print("[DEBUG] AC Started")
        self.running = True
        while self.running:
            self.mouse.click(self.button)
            time.sleep(self.interval)

        print("[DEBUG] AC Stopped")

    def stop(self):
        self.running = False


if __name__ == "__main__":
    print("You now have 3 seconds to move your mouse to the desired location")
    time.sleep(3)
    mouse = Controller()
    clicker = Clicker(0.25, mouse)
    clicker.start()
    time.sleep(5)
    clicker.stop()
    clicker.join()
    print("[DEBUG] AC Finished")
