import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time


if __name__ == "__main__":
    world = World(shape=(101, 51))

    wires = [
        Wire(start=(15, 40), stop=(80, 40), current=Current(x=1, y=0), voltage=9),
        Wire(start=(81, 40), stop=(85, 40), current=Current(x=1, y=0), voltage=0),
        Wire(start=(85, 39), stop=(85, 10), current=Current(x=0, y=-1), voltage=0),
        Wire(start=(81, 10), stop=(85, 10), current=Current(x=-1, y=0), voltage=0),
        Wire(start=(15, 10), stop=(80, 10), current=Current(x=-1, y=0), voltage=9),
        Wire(start=(15, 11), stop=(15, 39), current=Current(x=0, y=1), voltage=9)
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    now = time.time()
    world.compute(1000)
    print('The computation took', time.time() - now, 'seconds.')

    world.show_all()
    
