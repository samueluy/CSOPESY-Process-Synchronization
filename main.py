import threading
import fitting_room
import time

def run(color, fitting_room_instance):
    fitting_room_instance.enter(color)
    time.sleep(1)  # Simulate using the fitting room
    fitting_room_instance.leave()

def main():
    slots = int(input("Enter number of slots inside the fitting room: "))
    num_blue = int(input("Enter number of Blue threads: "))
    num_green = int(input("Enter number of Green threads: "))

    fitting_room_instance = fitting_room.FittingRoom(slots)

    threads = []
    for i in range(num_blue):
        t = threading.Thread(target=run, args=("blue", fitting_room_instance), name=f"Blue-Thread-{i+1}")
        threads.append(t)

    for i in range(num_green):
        t = threading.Thread(target=run, args=("green", fitting_room_instance), name=f"Green-Thread-{i+1}")
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()