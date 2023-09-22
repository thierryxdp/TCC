import math
def qtd_divisores(num):
    """Função que conta quantos divisores um número int tem; int -> int"""
    soma = 0
    for i in range(1, num + 1):
        if num % i == 0:
            soma = i
    return soma