from math import sqrt

def qtd_divisores(num):
    yield 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            yield i
            outro_divisor = num // i
            if outro_divisor != i:
                yield outro_divisor
    yield num