import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time


if __name__ == "__main__":
    world = World(shape=(200, 200))
    wires = [
        Wire(start=(40, 20), stop=(40, 180), current=Current(x=0, y=1), voltage=5),
        Wire(start=(40, 180), stop=(160, 180), current=Current(x=1, y=0), voltage=5),
        Wire(start=(160, 180), stop=(160, 160), current=Current(x=0, y=1), voltage=5),
        Wire(start=(160, 160), stop=(60, 160), current=Current(x=1, y=0), voltage=2.5),

        Wire(start=(60, 160), stop=(60, 110), current=Current(x=0, y=1), voltage=2.5),
        Wire(start=(60, 110), stop=(120, 110), current=Current(x=1, y=0), voltage=2.5),
        Wire(start=(120, 110), stop=(120, 90), current=Current(x=0, y=1), voltage=2.5),
        Wire(start=(120, 90), stop=(60, 90), current=Current(x=1, y=0), voltage=0),

        Wire(start=(60, 90), stop=(60, 20), current=Current(x=0, y=1), voltage=0),
        Wire(start=(60, 20), stop=(40, 20), current=Current(x=1, y=0), voltage=0),     
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    now = time.time()
    world.compute(1000)
    print('The computation took', time.time() - now, 'seconds.')

    world.show_all()