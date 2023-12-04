import threading
from FittingRoom import FittingRoom

# User input
n = int(input("Enter number of slots inside the fitting room: "))
b = int(input("Enter number of blue threads: "))
g = int(input("Enter number of green threads: "))

fitting_room = FittingRoom(n)  # Create a fitting room object
enter_threads = []  # Create a list of entering threads
leave_threads = []  # Create a list of leaving threads

print("**************************************\nProgram Start\n**************************************")

<<<<<<< HEAD
# Create blue entering threads
=======
#Special Case: No Threads.
if (b == 0 and g == 0):
    print("No threads. Fitting room is empty.")
elif (b <= 0 or g <= 0):
    print("Invalid number of threads.")
    
# Create blue threads
>>>>>>> d913c76c34d78abc7a8e85ea2f528742453f77d9
for i in range(b):
    enter_threads.append(threading.Thread(target=fitting_room.enter, args=('b',)))

# Create green entering threads
for i in range(g):
    enter_threads.append(threading.Thread(target=fitting_room.enter, args=('g',)))

# Start entering threads
for thread in enter_threads:
    thread.start()

# Wait for all entering threads to terminate
for thread in enter_threads:
    thread.join()

# Create blue leaving threads
for i in range(b):
    leave_threads.append(threading.Thread(target=fitting_room.leave, args=('b',)))

# Create green leaving threads
for i in range(g):
    leave_threads.append(threading.Thread(target=fitting_room.leave, args=('g',)))

# Start leaving threads
for thread in leave_threads:
    thread.start()

# Wait for all leaving threads to terminate
for thread in leave_threads:
    thread.join()

print("**************************************\nProgram End\n**************************************")
