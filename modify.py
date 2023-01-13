import random

def modify(code):
    codeList = [x for x in code]
    for loop in range(random.randint(0,10)):
        if random.choice([0,1]) == 0:
            codeList.pop(random.randint(0,len(codeList)-1))
        else:
            codeList.insert(random.randint(0,len(codeList)-1), random.choice(["<", ">", "+", "-", "}", "."]))
def newscript(length):
    code = ''
    for z in range(length):
        code+= random.choice(["<", ">", "+", "-", "}", "."])
    return code