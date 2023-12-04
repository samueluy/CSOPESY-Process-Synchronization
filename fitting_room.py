import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s',)

class FittingRoom:
    def __init__(self, n):
        self.slots = n
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.current_color = None
        self.occupancy = 0
        self.waiting = {'blue': 0, 'green': 0}

    def enter(self, color):
        thread_id = threading.current_thread().name
        with self.condition:
            self.waiting[color] += 1
            while (self.current_color is not None and self.current_color != color) or \
                  (self.current_color == color and self.occupancy == self.slots):
                self.condition.wait()
            self.waiting[color] -= 1
            self.occupancy += 1
            if self.occupancy == 1:
                logging.debug(f"\n{color.capitalize()} only.")
            self.current_color = color
            logging.debug(f"{thread_id} entered the fitting room.")

    def leave(self):
        thread_id = threading.current_thread().name
        with self.condition:
            self.occupancy -= 1
            if self.occupancy == 0:
                self.switch_turn()
                logging.debug("\nEmpty fitting room.")

    def switch_turn(self):
        next_color = 'green' if self.current_color == 'blue' else 'blue'
        if self.waiting[next_color] > 0:
            self.current_color = next_color
            self.condition.notify_all()
        elif self.waiting[self.current_color] > 0:
            self.condition.notify_all()
        else:
            self.current_color = None