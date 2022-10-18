import random


def modify(code):
    workspace = list(code)
    if len(workspace) > 0:
        for x in range(random.randint(0, 10)):
            z = random.randint(0, len(workspace)-1)
            select = random.randint(1, 3)
            # remove a character
            if select == 1:
                workspace.pop(z)

            # modify a character
            elif select == 2:
                workspace[z] = random.choice(
                    ("<", ">", "+", "-", "[", "]", ".", ","))

            # insert a charcter
            elif select == 3:
                workspace.insert(z, random.choice(
                    ("<", ">", "+", "-", "[", "]", ".", ",")))
            # splice a piece of code
            # elif select == 4:
                #chunks = code2[0].split('s')[0]
                # workspace.insert(z,[random.randint(0,len(chunks))-1])
    return [code[0], ''.join(workspace), code[2]]
