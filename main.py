import threading
import time
import random
from FittingRoom import FittingRoom  # Assume FittingRoom is in a separate file named fitting_room.py

def thread_behavior(fitting_room, color):
    fitting_room.enter(color)
    time.sleep(random.uniform(0.1, 1.0))  # Simulate time spent in the fitting room
    fitting_room.leave()

# User input for the number of slots and threads
n = int(input("Enter the number of slots inside the fitting room: "))
b = int(input("Enter the number of blue threads: "))
g = int(input("Enter the number of green threads: "))

fitting_room = FittingRoom(n)

print("**************************************\nProgram Start\n**************************************")

# Create blue and green threads
blue_threads = [threading.Thread(target=thread_behavior, args=(fitting_room, 'blue'), name=f"Blue-Thread-{i+1}") for i in range(b)]
green_threads = [threading.Thread(target=thread_behavior, args=(fitting_room, 'green'), name=f"Green-Thread-{i+1}") for i in range(g)]

# Start blue and green threads
for t in blue_threads + green_threads:
    t.start()

# Wait for all threads to finish
for t in blue_threads + green_threads:
    t.join()

print("**************************************\nProgram End\n**************************************")
