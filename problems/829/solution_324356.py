def soma_h(N):
    ''' retorna o valor H com N termos onde N é inteiro e dado como entrada;
    int -> float '''
    i = 0
    for elem in range(1,N+1):
        h = 1/elem
        i = i + h
    return round(i,2)