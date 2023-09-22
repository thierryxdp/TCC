def soma_h(N):
    '''função que calcula e retorna o valor H com N termos.
    int -> float'''
    cont = 0.0
    for i in range(1, N+1):
        cont = cont + 1/i
        return round(cont, 2)