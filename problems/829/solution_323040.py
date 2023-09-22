def soma_h(N):
    '''Função que calcula e retorna o valor H com N termos, onde N ́e inteiro e
́e dado como entrada.'''
    #int -> float
    soma = 0
    for numero in range(1, N + 1):
        soma += 1/numero
    return round(soma, 2)