def soma_h(N):
    """ Dado um número inteiro(N) qualquer retorna a soma de H=1+1/2+1/3...+1/N;
    int-> float """
    H=0
    for i in list(range(2,N)):
        H=H+1/i
    return round(H+1,2)