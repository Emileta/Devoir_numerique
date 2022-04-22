import env_examples
from examples.Text2wires import text2wire  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time


if __name__ == "__main__":
    '''Accepts any string of charcaters and converts it to a circuit'''

    circuit, x, y = text2wire('Salut louis')

    world = World(shape=(x, y))

    world.place(circuit)

    now = time.time()
    world.compute(1000)
    print('The computation took', time.time() - now, 'seconds.')
    
    world.show_all()
    
