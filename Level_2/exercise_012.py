# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

dados = [str(elem) for elem in range(1000,3000+1)]

todo_par = []

for elem in dados:
    if (int(elem[0]) % 2 == 0) and (int(elem[1]) % 2 == 0) and (int(elem[2]) % 2 == 0) and (int(elem[3]) % 2 == 0):
        todo_par.append(elem)

print(','.join(todo_par))