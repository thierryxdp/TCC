def soma_h(N):
    '''Funcao que calcula e retorna o valor H com N termos. int-> float'''
    soma = 0
    for a in range(1, N+1):
        inverso = (1/a)
        soma += inverso
    return round(soma, 2)