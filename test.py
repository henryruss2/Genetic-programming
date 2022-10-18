import interpret
import modify
import fitness

original = '+[+++++-+>++>++-++++++<<]>++.[+.]'
# if interpret interprets correctly
interpreted = interpret.interpret(original)[0]
if not interpreted == 'hi':
    print('interpreter problem')
print(interpreted)
# if modify changes the result
modified = modify.modify(original)
if modified == original:
    print('modify does not modify')
print(modified)
# if fitness gives a good fitness score for correct code
correctfitness = fitness.fitness(original)
if correctfitness <= 10:
    print('bad fitness')
print(correctfitness)