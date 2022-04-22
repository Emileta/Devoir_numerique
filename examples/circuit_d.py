import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time


if __name__ == "__main__":
    world = World(shape=(200, 200))
    wires = [
        Wire(start=(40, 20), stop=(40, 180), current=Current(x=0, y=0.619), voltage=100),
        Wire(start=(40, 180), stop=(160, 180), current=Current(x=0.619, y=0), voltage=100),
        Wire(start=(160, 180), stop=(160, 170), current=Current(x=0, y=-0.619), voltage=100),
        Wire(start=(160, 170), stop=(160, 160), current=Current(x=0, y=-0.619), voltage=38.095),
        Wire(start=(160, 160), stop=(160, 150), current=Current(x=0, y=-0.3809), voltage=38.095),
        Wire(start=(160, 150), stop=(160, 140), current=Current(x=0, y=-0.3809), voltage=0),
        Wire(start=(160, 160), stop=(60, 160), current=Current(x=-0.238, y=0), voltage=38.095),

        Wire(start=(60, 160), stop=(60, 135), current=Current(x=0, y=-0.238), voltage=38.095),
        Wire(start=(60, 135), stop=(60, 110), current=Current(x=0, y=-0.238), voltage=14.286),
        Wire(start=(60, 110), stop=(120, 110), current=Current(x=0.238, y=0), voltage=14.286),
        Wire(start=(120, 110), stop=(130, 110), current=Current(x=0.142, y=0), voltage=14.286),
        Wire(start=(130, 110), stop=(140, 110), current=Current(x=0.142, y=0), voltage=0),
        Wire(start=(120, 110), stop=(120, 100), current=Current(x=0, y=-0.095238), voltage=14.286),
        Wire(start=(120, 100), stop=(120, 90), current=Current(x=0, y=-0.095238), voltage=4.762),
        Wire(start=(120, 90), stop=(120, 80), current=Current(x=0, y=-0.047619), voltage=4.762),
        Wire(start=(120, 80), stop=(120, 75), current=Current(x=0, y=-0.047619), voltage=0),
        Wire(start=(120, 90), stop=(60, 90), current=Current(x=-0.047619, y=0), voltage=4.762),

        Wire(start=(60, 90), stop=(60, 30), current=Current(x=0, y=-0.047619), voltage=4.762),
        Wire(start=(60, 30), stop=(60, 20), current=Current(x=0, y=-0.047619), voltage=0),
        Wire(start=(60, 20), stop=(60, 15), current=Current(x=0, y=0.571429), voltage=0),
        Wire(start=(60, 20), stop=(50, 20), current=Current(x=-0.619, y=0), voltage=0),
        Wire(start=(50, 20), stop=(40, 20), current=Current(x=-0.619, y=0), voltage=100),  
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    now = time.time()
    world.compute(10000)
    print('The computation took', time.time() - now, 'seconds.')

    world.show_all()