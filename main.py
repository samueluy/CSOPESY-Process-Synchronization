import threading
from FittingRoom import FittingRoom

# User input
n = int(input("Enter number of slots inside the fitting room: "))
b = int(input("Enter number of blue threads: "))
g = int(input("Enter number of green threads: "))

fitting_room = FittingRoom(n) # Create a fitting room object
print("**************************************\nProgram Start\n**************************************")

# Create and start blue threads
b_threads = []
for i in range(b):
    b_threads.append(threading.Thread(target = fitting_room.enter, args = ('b',)))
    b_threads[-1].start()
for i in range(b):
    b_threads.append(threading.Thread(target = fitting_room.leave, args = ('b',)))
    b_threads[-1].start()

# Wait for all blue threads to terminate
for thread in b_threads:
    thread.join()

# Create and start green threads
g_threads = []
for i in range(g):
    g_threads.append(threading.Thread(target = fitting_room.enter, args = ('g',)))
    g_threads[-1].start()
for i in range(g):
    g_threads.append(threading.Thread(target = fitting_room.leave, args = ('g',)))
    g_threads[-1].start()

# Wait for all green threads to terminate
for thread in g_threads:
    thread.join()

print("**************************************\nProgram End\n**************************************")