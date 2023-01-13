def interpret(input, maxBytes=1000):
    code = str(input)
    i = 0
    failures= 0
    bytesRan = 0
    data = [0]
    pointer = 0
    output = ''
    while i < len(code) and bytesRan < maxBytes:
        try:
            # increment
            if code[i] == '+':
                data[pointer] += 1
            # decrement
            elif code[i] == '-':
                data[pointer] -= 1
            # move pointer right
            elif code[i] == '>':
                if pointer + 1 == len(data):
                    data.append(0)
                pointer += 1
            # move pointer left
            elif code[i] == '<':
                pointer -= 1
                pointer = abs(pointer)
            # add output to array
            elif code[i] == '.':
                output += chr(data[pointer]+1)
            # Jump to instruction
            elif code[i] == '}':
                i = data[pointer]
            i += 1
        except:
            failures+=1
        bytesRan += 1
    return [output, bytesRan, failures]