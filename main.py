from Graphing import *


def decay_input():
    while True:
        try:
            decay_chance = int(input("Enter a decay chance between 1 and 100 [integer %]: "))
            if decay_chance not in range(1,100):
                print("INVALID INPUT, TRY AGAIN: \n")
                decay_chance = "a"
            break
        except ValueError:
            print("INVALID INPUT, TRY AGAIN: \n")
            decay_chance =  -1
    return decay_chance


def atoms_input():
    while True:
        try:
            sample_size = int(input("Enter How many atoms are in the sample [integer atoms > 1]: "))
            if sample_size < 1:
                print("INVALID INPUT, TRY AGAIN: \n")
                sample_size = "a"
            break
        except ValueError:
            print("INVALID INPUT, TRY AGAIN: \n")
            sample_size = -1
    return sample_size


def main():
    chance = -1
    atoms = -1
    while chance not in range(1,100):
        chance = decay_input()
    while atoms < 2:
        atoms = atoms_input()

    add_graph(chance, atoms)

main()

