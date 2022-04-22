import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time


if __name__ == "__main__":
    world = World(shape=(50, 50))

    wires = [
        Wire(start=(10, 40), stop=(40, 40), current=Current(x=1, y=0), voltage=5),
        Wire(start=(40, 30), stop=(40, 10), current=Current(x=0, y=-1), voltage=10),
        Wire(start=(10, 10), stop=(40, 10), current=Current(x=-1, y=0), voltage=-5),
        Wire(start=(10, 30), stop=(10, 10), current=Current(x=0, y=1), voltage=10),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    now = time.time()
    world.compute(1000)
    print('The computation took', time.time() - now, 'seconds.')

    world.show_all()
    

    #world.show_all()
