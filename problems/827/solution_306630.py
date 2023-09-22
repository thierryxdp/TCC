from math import sqrt
def qtd_divisores(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i