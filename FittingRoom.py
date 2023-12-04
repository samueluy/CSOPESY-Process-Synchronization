import threading

class FittingRoom:
    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.current_slots = 0
        self.lock = threading.Lock()
        self.turn_condition = threading.Condition(self.lock)
        self.current_color = None

    def enter(self, color):
        with self.turn_condition:
            while (self.current_color is not None and self.current_color != color) or \
                  (self.current_color == color and self.current_slots >= self.num_slots):
                self.turn_condition.wait()
            
            self.current_slots += 1
            self.current_color = color
            print(f"{threading.current_thread().name} entered the fitting room.")

    def leave(self):
        with self.turn_condition:
            self.current_slots -= 1
            if self.current_slots == 0:
                self.current_color = None
                self.turn_condition.notify_all()
            print(f"{threading.current_thread().name} left the fitting room.")
