# find the fitness of a program
def fitness(program, intendedOut='demo'):
    try:
        fit = 0
        #subtract points based on the length of the program passed
        fit-= len(program.code) / 100
        #subtract points based on how long the program runs (in number of instructions)
        fit-= program.time /100
        #subtract points based on how many errors were thrown
        fit -= program.failures
        fit+= len(program.out.replace(intendedOut, '')) * 10
        #Find the total of a string using UTF-8
        def findTotal(text):
            total = 0
            for each in text:
                total += ord(each)
            return total
        #What the string total should be
        intendedTotal = findTotal(intendedOut)
        #what the outputed string total is
        outputtedTotal = findTotal(program.out)
        #subtract the difference between the two
        fit-= abs(intendedTotal-outputtedTotal)
        if program.out == 'intendedOut':
            print('SOLVED')
            print(program)
            raise ValueError
        return fit
    except:
        return -99999