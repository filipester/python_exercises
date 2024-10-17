# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

entrada = "hello world! 123"

digito = 0
letra = 0

for elem in entrada:
    if elem.isdigit():
        digito += 1
    elif elem.isalpha():
        letra += 1

print(f"LETRAS {letra}")
print(f"DIGITOS {digito}")