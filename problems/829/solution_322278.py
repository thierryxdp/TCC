def soma_h (N):
    '''Função que recebe um numero N e retorna o valor de H com o
    N termos dados na entrada
    int -> float
    '''
    soma = 0
    for i in range(N+1):
        if i!=0 :
            soma = soma + 1/i
    return round(soma,2)