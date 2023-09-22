def qtd_divisores (n: int)-> int:
    '''Retorna quantos divisores o número n dado possui'''
    qtd = 0
    for d in range(n+1):
        if d != 0 and n % d == 0:
            qtd = qtd + 1
    return qtd