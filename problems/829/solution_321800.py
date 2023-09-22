def soma_h(N):
    '''Função que recebe um numero inteiro N, calcula e retorna o valor de H com N termos. '''
    ''' int -> float '''
    H = 0
    for numeros in range(1, N + 1):
        H += 1/numeros
    return round(H, 2)