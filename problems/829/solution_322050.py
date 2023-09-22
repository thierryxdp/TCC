def soma_h(N):
    """ Dado um número inteiro(N) qualquer retorna a soma de H=1+1/2+1/3...+1/N;
    int-> float """
    i=0
    H=0
    for i in list(range(1,N)):
        H=H+1/list(range(1,N+1))[i]
        i=i+1
    return round(H+1,2)