import math
def qtd_divisores(num):
    """Função que conta quantos divisores um número int tem; int -> int"""
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += i
    return divisores