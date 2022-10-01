import random
import time

#interpreter to run the code, I have no clue how it works
def interpret(code):
    try:
        array = [0]
        result = ''
        pointerLocation = 0
        i = 0
        result = ''
        t1 = time.time()
        t= time.time()-t1
        while i < len(code) and t < 1:
            if code[i] == '<':
                if pointerLocation > 0:
                    pointerLocation -= 1
                    t = time.time() - t1
                    if t > 0.5:
                        return [result,code,t]
            elif code[i] == '>':
                pointerLocation += 1
                t = time.time() - t1
                if t > 0.5:
                        return [result,code,t]
                if len(array) <= pointerLocation:
                    array.append(0)
            elif code[i] == '+':
                array[pointerLocation] += 1
                t = time.time() - t1
                if t > 0.5:
                        return [result,code,t]
            elif code[i] == '-':
                if array[pointerLocation] > 0:
                    array[pointerLocation] -= 1
                t = time.time() - t1
                if t > 0.5:
                        return [result,code,t]
            elif code[i] == '.':
                result += chr(array[pointerLocation])
                t = time.time() - t1
                if t > 0.5:
                        return [result,code,t]
            elif code[i] == ',':
               #x = input("Input (1 CHARACTER!):")
                x = '0'
                try:
                    y = int(x)
                except ValueError:
                    y = ord(x)
                array[pointerLocation] = y
                t = time.time() - t1
                if t > 0.5:
                    return [result,code,t]
            elif code[i] == '[':
                if array[pointerLocation] == 0:
                    open_braces = 1
                    while open_braces > 0:
                        t = time.time() - t1
                        if t > 0.5:
                            return [result,code,t]
                        i += 1
                        if code[i] == '[':
                            open_braces += 1
                            t = time.time() - t1
                            if t > 0.5:
                                return [result,code,t]
                        elif code[i] == ']':
                            open_braces -= 1
                            t = time.time() - t1
                            if t > 0.5:
                                return [result,code,t]
            elif code[i] == ']':
                # you don't need to check array[pointerLocation] because the matching '[' will skip behind this instruction if array[pointerLocation] is zero
                open_braces = 1
                while open_braces > 0:
                    t = time.time() - t1
                    if t > 0.5:
                        return [result,code,t]
                    i -= 1
                    if code[i] == '[':
                        open_braces -= 1
                        t = time.time() - t1
                        if t > 0.5:
                            return [result,code,t]
                    elif code[i] == ']':
                        open_braces += 1
                        t = time.time() - t1
                        if t > 0.5:
                            return [result,code,t]
                # i still gets incremented in your main while loop
                i -= 1
            t= time.time()-t1
            if t > 0.5:
                return [result,code,t]
            i += 1
        t= time.time()-t1
        return [result[0:2],code,t]
    except:
            return ['failure:(',code,5]

#create a program
def generaterandom():
    generator = ""
    #find the length of the program
    for x in range(random.randint(1,100)):
        #pick a random character to add
        generator += random.choice(("<",">","+","-","[","]",".",","))
    return generator
NextGen = []
results = []
Solved = False
m = 0

#randomly edit the program
def modify(code):
    try:
        workspace = [x for x in code]
        for x in range(random.randint(0,10)):
            z = random.randint(0,len(workspace)-1)
            select = random.randint(1,3)
            #remove a character
            if select == 1:
                workspace.pop(z)
            
            #modify a character
            elif select == 2:
                workspace[z] = random.choice(("<",">","+","-","s[","]s",".",","))
            
            #insert a charcter
            elif select == 3:
                workspace.insert(z,random.choice(("<",">","+","-","[","]",".",",")))
            #splice a piece of code
            #elif select == 4:
                #chunks = code2[0].split('s')[0]
                #workspace.insert(z,[random.randint(0,len(chunks))-1])
        return ''.join(workspace)
    except:
        return ''

#create a list with 100 objects
for repeat in range(100):
    NextGen.append(generaterandom())

timer = time.time()

#find the fitness of code
def fitness(code):
    fit=0
    out = code[0]
    ind = 0
    if out == "failure:(":
        fit = -2
    if out == '':
        fit -= 1
    print(code)
    fit -= code[2]/10
    for char in out:
        if char == 'hi'[ind]:
            fit+=5
    for char2 in out:
        if char2 == 'h' or char2 == 'i':
            fit+=3
    fit+= abs(2-len(out))
    if len(out)> ind+1:
        ind+=1
    fit-= len(code[1])/100
    return fit

fitnesses = []
best = []
notfirsttime = False
#main loop
while Solved == False:
    #output the time of the generation
    print('time: ' + str(time.time()-timer))
    if notfirsttime:
        print(best[-1][0][0:2] + ' ' + str(fitnesses[-1]))
    else:
        notfirsttime = True
    m = 0
    #run the code
    for l in range(len(NextGen)):
        bfcode = NextGen[l]
        #try running the code
        try:
            results.append(interpret(bfcode))
        #if it fails give it a bad score
        except:
            results.append(['failure:(',bfcode,5])
    highscore = -100
    NextGen = []
    for each in range(len(results)):
        fit = fitness(results[each])
        #find the best code
        if fit > highscore:
            highscore = fit
            best.append(results[each])
        if results[each][0][0:2] == 'hi':
            solved =True
            finalcode = results[each][1]
            #print(finalcode)
            break
        fitnesses.append(fit)
    while len(best) > 100:
        best.pop(0)
    while len(best) < 100:
        best.append(best[-1])
    NextGen = []
    for c in best:
        current = c[0]
        NextGen.append(modify(current))