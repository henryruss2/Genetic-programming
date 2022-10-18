import time


def interpret(code):
    try:
        array = [0]
        result = ''
        pointerLocation = 0
        i = 0
        result = ''
        t1 = time.time()
        t = time.time()-t1
        while i < len(code) and t < 1:
            if code[i] == '<':
                if pointerLocation > 0:
                    pointerLocation -= 1
                    t = time.time() - t1
                    if t > 0.5:
                        return [result, code, t]
            elif code[i] == '>':
                pointerLocation += 1
                t = time.time() - t1
                if t > 0.5:
                    return [result, code, t]
                if len(array) <= pointerLocation:
                    array.append(0)
            elif code[i] == '+':
                array[pointerLocation] += 1
                t = time.time() - t1
                if t > 0.5:
                    return [result, code, t]
            elif code[i] == '-':
                if array[pointerLocation] > 0:
                    array[pointerLocation] -= 1
                t = time.time() - t1
                if t > 0.5:
                    return [result, code, t]
            elif code[i] == '.':
                result += chr(array[pointerLocation])
                t = time.time() - t1
                if t > 0.5:
                    return [result, code, t]
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
                    return [result, code, t]
            elif code[i] == '[':
                if array[pointerLocation] == 0:
                    open_braces = 1
                    while open_braces > 0:
                        t = time.time() - t1
                        if t > 0.5:
                            return [result, code, t]
                        i += 1
                        if code[i] == '[':
                            open_braces += 1
                            t = time.time() - t1
                            if t > 0.5:
                                return [result, code, t]
                        elif code[i] == ']':
                            open_braces -= 1
                            t = time.time() - t1
                            if t > 0.5:
                                return [result, code, t]
            elif code[i] == ']':
                # you don't need to check array[pointerLocation] because the matching '[' will skip behind this instruction if array[pointerLocation] is zero
                open_braces = 1
                while open_braces > 0:
                    t = time.time() - t1
                    if t > 0.5:
                        return [result, code, t]
                    i -= 1
                    if code[i] == '[':
                        open_braces -= 1
                        t = time.time() - t1
                        if t > 0.5:
                            return [result, code, t]
                    elif code[i] == ']':
                        open_braces += 1
                        t = time.time() - t1
                        if t > 0.5:
                            return [result, code, t]
                # i still gets incremented in your main while loop
                i -= 1
            t = time.time()-t1
            if t > 0.5:
                return [result, code, t]
            i += 1
        t = time.time()-t1
        return [result, code, t]
    except:
        return [':(', code, 5]
