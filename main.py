import threading
import fitting_room
import time
import random

def run(color, fitting_room_instance):
    fitting_room_instance.enter(color)
    time.sleep(1)  # Simulate using the fitting room
    fitting_room_instance.leave()

def main():
    slots = int(input("Enter number of slots inside the fitting room: "))
    num_blue = int(input("Enter number of Blue threads: "))
    num_green = int(input("Enter number of Green threads: "))

    fitting_room_instance = fitting_room.FittingRoom(slots)

    blue_threads = [threading.Thread(target=run, args=("blue", fitting_room_instance), name=f"Blue-Thread-{i+1}") for i in range(num_blue)]
    green_threads = [threading.Thread(target=run, args=("green", fitting_room_instance), name=f"Green-Thread-{i+1}") for i in range(num_green)]

    # Randomly decide which color group to start first
    if random.choice(['blue', 'green']) == 'blue':
        threads = blue_threads + green_threads
    else:
        threads = green_threads + blue_threads

    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()