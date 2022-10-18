import random
import time
import fitness
import modify
import interpret
import newscript


NextGen = []
results = []
Solved = False
m = 0


# create a list with 100 objects
for repeat in range(100):
    NextGen.append(newscript.generaterandom())

timer = time.time()

fitnesses = []
best = []
notfirsttime = False
# main loop
while Solved == False:
    # output the time of the generation
    print('time: ' + str(time.time()-timer))
    if notfirsttime:
        print('best: ' + best[-1][0][0:2] + ' fitness: ' + str(fitnesses[-1]))
    else:
        notfirsttime = True
    m = 0
    # run the code
    for l in range(len(NextGen)):
        bfcode = NextGen[l-1]
        # try running the code
        try:
            results.append(interpret.interpret(bfcode))
        # if it fails give it a bad score
        except:
            results.append([':(', bfcode, 5])
    highscore = -100
    NextGen = []
    for each in range(len(results)):
        fit = fitness.fitness(results[each-1])
        # find the best code
        if fit > highscore:
            highscore = fit
            best.append(results[each-1])
        if results[each-1][0][0:2] == 'hi':
            solved = True
            finalcode = results[each-1][1]
            print(finalcode)
            break
        fitnesses.append(fit)
    while len(best) > 100:
        best.pop(0)
    while len(best) < 100:
        best.append(best[-1])
    NextGen = []
    for c in best:
        #current = c[0]
        NextGen.append(modify.modify(c))
