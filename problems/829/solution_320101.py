def soma_h(n):
    '''Dado um número retorna no valor H com N termos,
    onde N é o inteiro dado.
    int --> float'''
    prox = 1
    total = 0
    while prox < n+1:
        total = total + 1/prox
        prox = prox+1
    return round(total,2)