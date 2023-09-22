def soma_h(N):
    '''função que recebe um número inteiro e retorna
    uma soma H dada pela equação ao lado
    int -> float
    '''
    soma = 0
    for n in range(1,N+1):
        soma += 1/n
    return round(soma,2)