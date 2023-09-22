def fatorial(n):
    "Função que dado um número n retorna seu fatorial. int --> int"
    if n == 0:
        return 1
    res = n
    while n > 2:
        n = n - 1 
        res = res * n
    return res