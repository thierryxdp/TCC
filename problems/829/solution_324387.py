def soma_h(N):
    '''Função que calcula a Soma H de um certo numero N, dado de entrada esse numero
    int -> float'''
    i = 0
    for elem in range(1,N+1):
        h = 1/elem
        i = i + h
    return round(i,2)