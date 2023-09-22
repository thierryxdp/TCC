def soma_h(N):
    '''Funcao que calcula e retorna o valor de H com N termos
    int -> float'''
    total = []
    for i in range(1,N+1):
        total.append(1/i)
    soma = sum(total)
    return round(soma,2)