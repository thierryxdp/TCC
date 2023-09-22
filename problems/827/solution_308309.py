def qtd_divisores(n):
    """Dado um número n retorna o número de divisores de n
    int-->int"""
    a = []
    i = 1
    while i <= n:
        if n%i == 0:
            a = a + [i]
        i = i + 1
    return len(a)