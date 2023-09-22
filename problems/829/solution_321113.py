def soma_h(N):
    '''Dado um numero inteiro N, retorna o valor H com os N termos.
    Retorna o resultado somente com 2 casas decimais.
    int -> float'''
    H=0
    for i in range(1,N+1):
        H=H+(1/i)
    return H