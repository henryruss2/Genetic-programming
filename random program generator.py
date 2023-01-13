import fitness
import modify
import interpret
intendedOut = 'demo'
#Define the program
class script:
    def __init__(self, code):
        #create a new program
        self.code = code
        #Interpret the program
        self.interpreted = interpret.interpret(self.code)
        #set the output and the time it takes for it to run, as well as the number of instructions that failed
        self.out = self.interpreted[0]
        self.time = self.interpreted[1]
        self.failures = self.interpreted[2]
        #self.fitness = fitness.fitness(self, intendedOut)
scripts = []
#create the scripts
for i in range(1000):
    nextScript = script(modify.newscript(64))
    scripts.append(nextScript)
#main loop
while True:
    #sort the scripts based on fitness
    scripts.sort(key=fitness.fitness)
    scripts.pop()
    #The next scripts
    newscripts = []
    #modify the scripts
    for i in range(1000):
        #make a copy of scripts 899 to 999 modified
        scriptNumber = i % 100
        scriptNumber = 0 - scriptNumber
        nextScript = script(modify.modify(scripts[scriptNumber].code))
        newscripts.append(nextScript)
    #replace the scripts with the new scripts
    scripts = newscripts
    #print the best script
    print(scripts[-1])