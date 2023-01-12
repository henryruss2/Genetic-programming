import time
import fitness
import modify
import interpret
import random

#Define the program
class script:
    def __init__(self, code):
        #create a new program
        self.code = code
        #Interpret the program
        self.interpreted = interpret.interpret()
        #set the output and the time it takes for it to run
        self.out = self.interpreted[0]
        self.time = self.interpreted[1]
    def __str__(self):
        return self.code
scripts = []
for i in range(1000):
    scripts.append(script(modify.newscript(64)))
solved = False
while solved == False:
    scripts.sort(key=fitness.fitness)