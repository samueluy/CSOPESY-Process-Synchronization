import threading
from FittingRoom import FittingRoom


# For quicker testing
# n = 5
# b = 3
# g = 3

# User input
n = int(input("Enter number of slots inside the fitting room: "))
b = int(input("Enter number of blue threads: "))
g = int(input("Enter number of green threads: "))

fitting_room = FittingRoom(n) # Create a fitting room object
threads = [] # Create a list of threads
print("**************************************\nProgram Start\n**************************************")

#Special Case: No Threads.
if (b == 0 and g == 0):
    print("No threads. Fitting room is empty.")
elif (b <= 0 or g <= 0):
    print("Invalid number of threads.")
    
# Create blue threads
for i in range(b):
    threads.append(threading.Thread(target = fitting_room.enter, args = ('b',)))
    threads.append(threading.Thread(target = fitting_room.leave, args = ('b',)))

# Create green threads
for i in range(g):
    threads.append(threading.Thread(target = fitting_room.enter, args = ('g',)))
    threads.append(threading.Thread(target = fitting_room.leave, args = ('g',)))

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to terminate
for thread in threads:
    thread.join()

print("**************************************\nProgram End\n**************************************")