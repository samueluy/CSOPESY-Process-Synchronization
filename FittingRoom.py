import threading

class FittingRoom:
    def __init__(self, num_threads):
        self.n = num_threads
        self.b_slots = 0  # Number of blue slots
        self.g_slots = 0  # Number of green slots
        self.b_lock = threading.Lock()  # Lock blue
        self.g_lock = threading.Lock()  # Lock green
        self.fr_lock = threading.Lock()  # Lock the entire room
        self.b_cond = threading.Condition(self.b_lock)  # Condition variable for blue
        self.g_cond = threading.Condition(self.g_lock)  # Condition variable for green

    def enter(self, color):
        with self.fr_lock:  # Lock the entire room
            if color == 'b':  # Blue thread enters
                if self.b_slots == 0 and self.g_slots == 0:  # If the room is empty
                    print("Blue only.")
                self.b_slots += 1  # Increment number of blue slots
                if self.b_slots == 1:  # If blue thread is the first to enter
                    self.g_lock.acquire()  # Acquire the green lock
            else:
                if self.b_slots == 0 and self.g_slots == 0:  # If the room is empty
                    print("Green only.")
                self.g_slots += 1  # Increment number of green slots
                if self.g_slots == 1:  # If green thread is the first to enter
                    self.b_lock.acquire()  # Acquire the blue lock

        print(f"{threading.current_thread().name} - {color} thread entered fitting room")

    def leave(self, color):
        with self.fr_lock:  # Lock the entire room
            if color == 'b':  # Blue thread leaves
                self.b_slots -= 1  # Decrement number of blue slots
                if self.b_slots == 0:  # If blue thread is the last to leave
                    self.g_lock.release()  # Release the green lock
            else:
                self.g_slots -= 1  # Decrement number of green slots
                if self.g_slots == 0:  # If green thread is the last to leave
                    self.b_lock.release()  # Release the blue lock

        if self.b_slots == 0 and self.g_slots == 0:  # If the room is empty
            print("Empty fitting room.")
        else:
            print(f"{threading.current_thread().name} - {color} thread left fitting room")

    

