import random


def generaterandom():
    generator = ""
    # find the length of the program
    for x in range(random.randint(1, 100)):
        # pick a random character to add
        generator += random.choice(("<", ">", "+", "-", "[", "]", ".", ","))
    return generator
