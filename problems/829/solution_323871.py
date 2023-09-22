def soma_h(N):
    ''' função que calcula e retorna o valor H de N termos
    int -> float
    '''
    lista_soma = []
    
    for numero in range(2, N+1):
        lista_soma.append((numero)**-1)
    soma = sum(lista_soma)
    return round(soma, 2)