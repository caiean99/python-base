#!/usr/bin/env python3

"""Imprime a tabuada de 1 ao 10
---Tabuada do 1---
1 x 1 = 1
1 x 2 = 2
3 x 3 = 3
...
##################
"""

__version__ = "0.1.1"
__author__ = "Kaduza1"

template = """
1---

{bloco:^19}

##################
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2 
        print("{:^20}".format(f"{n1} x {n2} = {resultado}"))     
    print()
    print("#" * 20)
    print()
