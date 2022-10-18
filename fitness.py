def fitness(code):
    fit = 0
    out = code[0][0:2]
    ind = 0
    if out == ":(":
        fit = -2
    if out == '':
        fit -= 1
    print(code)
    fit -= code[2]/100
    for char in out:
        if char == 'hi'[ind]:
            fit += 5
    for char2 in out:
        if char2 == 'h' or char2 == 'i':
            fit += 3
    fit += abs(2-len(out))
    if len(out) > ind+1:
        ind += 1
    fit -= len(code[1])/100
    return fit
