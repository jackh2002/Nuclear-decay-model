import matplotlib.pyplot as plt
import numpy as np
import random


def decay_sim(decay_chance, current_atoms):
    decayed_atom = 0
    for atom in range(0, current_atoms):
        rand_value = random.randint(0, 99)
        if rand_value <= decay_chance:
            decayed_atom += 1
    return (current_atoms - decayed_atom)


def decay_prediction(decay_chance, initial_atoms,x):
    return initial_atoms * np.exp(-1*(decay_chance/100)*x)


def plot(trend, data,chance):
    plt.ylabel("Unstable atoms")
    plt.xlabel("Decay cycles")
    plt.plot(np.arange(0,len(data)), trend, label="Exponential model",color="black")
    plt.plot(np.arange(0,len(data)), data, label="Random decay", linestyle="none",marker="x",color="orange")
    plt.legend()
    plt.title("Atoms:  "+str(trend[0])+",  Decay chance:  "+str(chance)+"%")
    plt.show()


def data_generation(decay_chance, initial_atoms):
    decays = 0
    unstable_atoms = initial_atoms
    prediction = [initial_atoms]
    simulation = [initial_atoms]
    while simulation[decays] > 0 and simulation[decays] > 0.001*simulation[0]:
        decays += 1
        prediction.append(decay_prediction(decay_chance, initial_atoms, decays))
        simulation.append(decay_sim(decay_chance, simulation[decays-1]))
        #print(simulation[len(simulation)-1])
    return [prediction, simulation]


def add_graph(decay_chance, initial_atoms):
    data = data_generation(decay_chance, initial_atoms)
    plot(data[0], data[1],decay_chance)


