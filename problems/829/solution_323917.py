def soma_h(N):
    '''Função que calcula e retorna o valor H com N termos onde N é inteiro. H = 1 + 1/2 + ... + 1/N.
    int -> float'''
    valorH = 0
    for i in range(1, N + 1):
        inverso = (1/i)
        valorH = valorH + inverso
    return round(valorH,2)