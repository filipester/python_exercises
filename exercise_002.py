# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num-1)
    
numero = 8

print(fatorial(8))