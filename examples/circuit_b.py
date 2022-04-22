import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time


if __name__ == "__main__":
    world = World(shape=(51,51))

    wires = [
        Wire(start=(10, 40), stop=(35, 40), current=Current(x=1, y=0), voltage=9),
        Wire(start=(36, 40), stop=(40, 40), current=Current(x=1, y=0), voltage=0),
        Wire(start=(40, 39), stop=(40, 10), current=Current(x=0, y=-1), voltage=0),
        Wire(start=(16, 10), stop=(39, 10), current=Current(x=-1, y=0), voltage=0),
        Wire(start=(10, 10), stop=(15, 10), current=Current(x=-1, y=0), voltage=9),
        Wire(start=(10, 11), stop=(10, 39), current=Current(x=0, y=1), voltage=9)
    ]


    circuit = Circuit(wires=wires)

    world.place(circuit)

    now = time.time()
    world.compute(1000)
    print('The computation took', time.time() - now, 'seconds.')

    world.show_all()
    
