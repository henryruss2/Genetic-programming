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
                    if t > 1:
                        return [result,code,t]
            elif code[i] == '>':
                pointerLocation += 1
                t = time.time() - t1
                if t > 1:
                        return [result,code,t]
                if len(array) <= pointerLocation:
                    array.append(0)
            elif code[i] == '+':
                array[pointerLocation] += 1
                t = time.time() - t1
                if t > 1:
                        return [result,code,t]
            elif code[i] == '-':
                if array[pointerLocation] > 0:
                    array[pointerLocation] -= 1
                t = time.time() - t1
                if t > 1:
                        return [result,code,t]
            elif code[i] == '.':
                result += chr(array[pointerLocation])
                t = time.time() - t1
                if t > 1:
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
                if t > 1:
                    return [result,code,t]
            elif code[i] == '[':
                if array[pointerLocation] == 0:
                    open_braces = 1
                    while open_braces > 0:
                        t = time.time() - t1
                        if t > 1:
                            return [result,code,t]
                        i += 1
                        if code[i] == '[':
                            open_braces += 1
                            t = time.time() - t1
                            if t > 1:
                                return [result,code,t]
                        elif code[i] == ']':
                            open_braces -= 1
                            t = time.time() - t1
                            if t > 1:
                                return [result,code,t]
            elif code[i] == ']':
                # you don't need to check array[pointerLocation] because the matching '[' will skip behind this instruction if array[pointerLocation] is zero
                open_braces = 1
                while open_braces > 0:
                    t = time.time() - t1
                    if t > 1:
                        return [result,code,t]
                    i -= 1
                    if code[i] == '[':
                        open_braces -= 1
                        t = time.time() - t1
                        if t > 1:
                            return [result,code,t]
                    elif code[i] == ']':
                        open_braces += 1
                        t = time.time() - t1
                        if t > 1:
                            return [result,code,t]
                # i still gets incremented in your main while loop
                i -= 1
            t= time.time()-t1
            if t > 1:
                return [result,code,t]
            i += 1
        t= time.time()-t1
        return [result,code,t]
    except:
            return ['failure:(',bfcode,5]

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
def modify(code,code2):
        workspace = [x for x in code]
        for x in range(random.randint(1,10)):
            z = random.randint(0,len(workspace)-1)
            select = random.randint(1,4)
            #remove a character
            if select == 1:
                workspace.pop(z)
            
            #modify a character
            elif select == 2:
                workspace[z] = random.choice(("\<","\>","\+","\-","s\[","\]s","\.","\,"))
            
            #insert a charcter
            elif select == 3:
                workspace.insert(z,random.choice(("\<","\>","\+","\-","\[","\]","\.","\,")))
            
            #splice a piece of code
            elif select == 4:
                chunks = code2[1].split('s')
                workspace.insert(z,[random.randint(0,len(chunks))-1])
        return workspace

#create a list with 100 objects
for repeat in range(100):
    NextGen.append(generaterandom())

#make sure it has 100 objects
while len(NextGen) <= 100:
    NextGen.append(generaterandom())
timer = time.time()

fitnesses = []
#main loop
while Solved == False:
    #print the time of the generation
    print('time: ' + str(time.time()-timer))
    timer = time.time()
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
    highscore = -10
    best = []
    NextGen = []
    #find the fitness
    for each in results:
        fit=0
        final = each[0]
        ind = 0
        indecks = 0
        if final == "failure:(":
            fit = -2
        if final == '':
            fit -= 1
        fit -= each[2]/10
        for char in final:
            if char == 'hi'[ind]:
                fit+=5
        for char2 in final:
            if char2 == 'h' or char2 == 'i':
                fit+=1
            
        if len(final)> ind+1:
            ind+=1
        else:
              continue
        if fit > highscore:
            highscore = fit
            best.append(each[1])
            if each[0] == 'hello world':
                solved =True
                finalcode = each[1]
                print(finalcode)
        fitnesses.append(fit)
    while len(best) > 100:
        best.pop(0)
    while len(best) < 100:
        print(len(best))
        best.append(best[-1])
    NextGen = []
    for current in best:
        NextGen.append(modify(current, best[best.index(current)-1]))
    print('best output: ' + str(best[-1][1]) + ' score:' + str(fitnesses[-1]))
