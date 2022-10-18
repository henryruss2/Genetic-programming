def interpret(code):
    try:
        array = [0]
        result = ''
        pointerLocation = 0
        i = 0
        result = ''
        iter = 0
        while i < len(code) and iter < 1000:
            if code[i] == '<':
                if pointerLocation > 0:
                    pointerLocation -= 1
                    iter += 1
                if iter > 100:
                    return [result, code, iter]
            elif code[i] == '>':
                pointerLocation += 1
                iter += 1
                if iter > 100:
                    return [result, code, iter]
                if len(array) <= pointerLocation:
                    array.append(0)
            elif code[i] == '+':
                array[pointerLocation] += 1
                iter += 1
                if iter > 100:
                    return [result, code, iter]
            elif code[i] == '-':
                if array[pointerLocation] > 0:
                    array[pointerLocation] -= 1
                iter += 1
                if iter > 100:
                    return [result, code, iter]
            elif code[i] == '.':
                result += chr(array[pointerLocation])
                iter += 1
                if iter > 100:
                    return [result, code, iter]
            elif code[i] == ',':
               #x = input("Input (1 CHARACTER!):")
                x = '0'
                try:
                    y = int(x)
                except ValueError:
                    y = ord(x)
                array[pointerLocation] = y
                iter += 1
                if iter > 100:
                    return [result, code, iter]
            elif code[i] == '[':
                if array[pointerLocation] == 0:
                    open_braces = 1
                    while open_braces > 0:
                        iter += 1
                        if iter > 100:
                            return [result, code, iter]
                        i += 1
                        if code[i] == '[':
                            open_braces += 1
                            iter += 1
                            if iter > 100:
                                return [result, code, iter]
                        elif code[i] == ']':
                            open_braces -= 1
                            iter += 1
                            if iter > 100:
                                return [result, code, iter]
            elif code[i] == ']':
                # you don't need to check array[pointerLocation] because the matching '[' will skip behind this instruction if array[pointerLocation] is zero
                open_braces = 1
                while open_braces > 0:
                    iter += 1
                    if iter > 1000:
                        return [result, code, iter]
                    i -= 1
                    if code[i] == '[':
                        open_braces -= 1
                        iter += 1
                        if iter > 100:
                            return [result, code, iter]
                    elif code[i] == ']':
                        open_braces += 1
                        iter += 1
                        if iter > 100:
                            return [result, code, iter]
                # i still gets incremented in your main while loop
                i -= 1
            if iter > 100:
                return [result, code, iter]
            i += 1
        return [result, code, iter]
    except:
        return [result, code, iter]
