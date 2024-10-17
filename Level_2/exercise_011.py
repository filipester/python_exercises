# Write a program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# 0000,0010,0101,0110,1010,1101,1000,1111,0100,1001

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# numeros = [x for x in input("Digite os números separados por virgulas: ").split(',')] # isso já funciona
numeros = "0000,0010,0101,0110,1010,1101,1000,1111,0100,1001".split(',')

divisiveis = [elem for elem in numeros if (int(elem,2) % 5 == 0)]

print(f"Sequência de binários: {numeros}")

print(" ".join(divisiveis))
convertidos = [int(x, 2) for x in divisiveis]
print(f"Conversão para inteiros: {convertidos}")
