import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World
import time

def text2wire(string):
    '''Creates wires from a given string of caracters,
    The goal is to create circuits of any sentence simply as a fun quirk,
    there is no physical significance and it is a cool easteregg (yes it was done at during easter brake).'''
    string = string.upper()
    wire_shape = Wire(start=(10, 40), stop=(35, 40), current=Current(x=1, y=0), voltage=9)
    wires = []
    alphabet_dicti = {
        'A':[(0, 0), (0, 35), (20, 35), (20, 0), (15, 0), (15, 20), (5, 20), (5, 25), (15, 25), (15, 30), (5, 30), (5, 0)], 
        'B':[(0,0),(0,35),(20,35),(20,0),(15,0),(15,30),(5,30),(5,20),(15,20),(15,15),(5,15),(5,10),(15,10),(15,0)],
        'C':[(0, 0), (0, 35), (20, 35), (20, 30), (5, 30), (5, 5), (20, 5), (20, 0)],
        'D':[(0, 0), (0, 35), (20, 35), (20, 30), (5, 30), (5, 5), (15, 5), (15, 30), (20, 30), (20, 0)],
        'E':[(0, 0), (0, 35), (20, 35), (20, 30), (5, 30), (5, 20), (10, 20), (10, 15), (5, 15), (5, 5), (20, 5), (20, 0)],
        'F':[(0, 0), (0, 35), (20, 35), (20, 30), (5, 30), (5, 20), (10, 20), (10, 15), (5, 15), (5, 0)],
        'G':[(0, 0), (0, 35), (20, 35), (20, 30), (5, 30), (5, 20), (20, 20), (20, 0), (15, 0), (15, 15), (5, 15), (5, 5), (15, 5), (15, 0), (5, 0)],
        'H':[(0, 0), (0, 35), (5, 35), (5, 20), (15, 20), (15, 35), (20, 35), (20, 0), (15, 0), (15, 15), (5, 15), (5, 0)],
        'I':[(0, 0), (0, 5), (5, 5), (5, 30), (0, 30), (0, 35), (15, 35), (15, 30), (10, 30), (10, 5), (15, 5), (15, 0)],
        'J':[(0, 0), (0, 10), (5, 10), (5, 5), (15, 5), (15, 35), (20, 35), (20, 0)],
        'K':[(0, 0), (0, 35), (5, 35), (5, 20), (10, 20), (10, 15), (5, 15), (5, 0)],
        'L':[(0, 0), (0, 35), (5, 35), (5, 5), (20, 5), (20, 0)],
        "M":[(0, 0), (0, 35), (5, 35), (5, 30), (15, 30), (15, 35), (20, 35), (20, 0), (15, 0), (15, 25), (12, 25), (12, 20), (8, 20), (8, 25), (5, 25), (5, 0)],
        'N':[(0, 0), (0, 35), (5, 35), (5, 30), (10, 30), (10, 20), (15, 20), (15, 35), (20, 35), (20, 0), (15, 0), (15, 5), (10, 5), (10, 15), (5, 15), (5, 0)],
        'O':[(0, 0), (0, 35), (20, 35), (20, 0), (15, 0), (15, 30), (5, 30), (5, 5), (15, 5), (15, 0)],
        'P':[(0, 0), (0, 35), (20, 35), (20, 20), (5, 20), (5, 30), (15, 30), (15, 25), (5, 25), (5, 0)],
        'Q':[(0, 0), (0, 35), (20, 35), (20, 5), (25, 5), (25, 0), (15, 0), (15, 30), (5, 30), (5, 5), (15, 5), (15, 0)],
        'R':[(0, 0), (0, 35), (20, 35), (20, 25), (15, 25), (15, 30), (5, 30), (5, 25), (20, 25), (20, 5), (15, 5), (15, 20), (5, 20), (5, 0)],
        'S':[(0, 0), (0, 5), (15, 5), (15, 15), (0, 15), (0, 35), (20, 35), (20, 30), (5, 30), (5, 20), (20, 20), (20, 0)],
        'T':[(10, 0), (10, 30), (0, 30), (0, 35), (20, 35), (20, 30), (15, 30), (15, 0)],
        'U':[(0, 0), (0, 35), (5, 35), (5, 5), (15, 5), (15, 35), (20, 35), (20, 0)],
        'V':[(0, 0), (0, 35), (5, 35), (5, 5), (15, 5), (15, 35), (20, 35), (20, 0)],
        'W':[(0, 0), (0, 35), (5, 35), (5, 5), (8, 5), (8, 15), (12, 15), (12, 5), (15, 5), (15, 35), (20, 35), (20, 0)],
        ' ':[]
                    }
    for i in range(len(string)):
        letter_points = alphabet_dicti[string[i]]
        print(string[i])
        for j in range(len(letter_points)):
            if j < len(letter_points) - 1:
                if letter_points[j][0] == letter_points[j + 1][0]:
                    if letter_points[j][1] < letter_points[j + 1][1]:
                        wires.append(Wire(start=(letter_points[j][0] + i * (20+2) + 5, letter_points[j][1]+5), stop= (letter_points[j+1][0] + i * ( 20+2) + 5, letter_points[j+1][1]+5), current=Current(x=0, y=1), voltage=i+1 ))
                    else:
                        wires.append(Wire(start=(letter_points[j][0] + i * (20+2) + 5, letter_points[j][1]+5), stop= (letter_points[j+1][0] + i * ( 20+2) + 5, letter_points[j+1][1]+5), current=Current(x=0, y=-1), voltage=i+1 ))
                else:
                    if letter_points[j][0] < letter_points[j + 1][0]:
                        wires.append(Wire(start=(letter_points[j][0] + i * (20+2) + 5, letter_points[j][1]+5), stop= (letter_points[j+1][0] + i * ( 20+2) + 5, letter_points[j+1][1]+5), current=Current(x=1, y=0), voltage=i+1 ))
                    else:
                        wires.append(Wire(start=(letter_points[j][0] + i * (20+2) + 5, letter_points[j][1]+5), stop= (letter_points[j+1][0] + i * ( 20+2) + 5, letter_points[j+1][1]+5), current=Current(x=-1, y=0), voltage=i+1 ))
            else:
                wires.append(Wire(start=(letter_points[j][0] + i * (20+2) + 5, letter_points[j][1]+5), stop= (letter_points[0][0] + i *  (20 +2) + 5, letter_points[0][1]+5), current=Current(x=-1, y=0), voltage=i+1 ))
    size_x = len(string) * 22 + 20
    size_y = 45
    print('Le size du world est:' + f'{size_x, size_y}')
    return Circuit(wires), size_x, size_y
