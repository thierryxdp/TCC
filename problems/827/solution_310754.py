from math import sqrt

def qtd_divisores(num):
    yield 1 # 1 é divisor de qualquer número
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            yield i # encontrei um divisor
            outro_divisor = num // i
            if outro_divisor != i: # não é quadrado perfeito
                yield outro_divisor # retorna o outro divisor
    yield num # o próprio número é divisor dele mesmo