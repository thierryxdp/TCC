def soma_h(N):
    '''Funcao que calcula e retorna o valor de H com N termos'''
    '''int -> float'''
    soma = 0
    for c in range(1, N + 1):
        inverso = (1/c)
        soma = soma + inverso
    return round(soma, 2)