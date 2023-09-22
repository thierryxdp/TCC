def soma_h(N):
    '''função calcula o somatório dos inversos de 1 até N
    int -> float'''
    k = 1
    for i in range(2,N+1):
        k += 1/i
    return round(k, 2)