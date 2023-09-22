import math
def qtd_divisores(n):
    """Função que dado um número n, calcula sua
    quantidade de divisores; int -> int"""
    if n < 0:
        return 0
    div = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            div.extend([i,n/i])
    div.extend([n])
    return len(set(div))