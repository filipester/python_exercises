# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: 
# Consider use range(#begin, #end) method

lista_total = list(range(2000, 3201))

lista_mod = []

for elem in lista_total:
    if elem % 7 == 0 and elem % 5 != 0:
        lista_mod.append(elem)

print(lista_mod)