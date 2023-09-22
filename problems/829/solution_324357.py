def soma_h(N):
    '''função em que dado um número inteiro (N) retorne o seu somatório;
    int -> float'''
    s=0
    for i in range(1,N+1):
        s+=(1/i)
    return round(s,2)