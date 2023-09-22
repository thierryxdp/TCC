from math import sqrt
def qtd_divisores(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i
            outro_divisor = num // i
            if outro_divisor != i:
                return outro_divisor
    return num