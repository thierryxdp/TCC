def fatorial(n):
    'funcao pega um numero e calcula o numero fatorial dele int-->int'
    for i in range(n-1,0,-1):
        n = n * i
    return n