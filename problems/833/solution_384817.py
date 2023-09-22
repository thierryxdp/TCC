def conta_numero(numero, matriz):
    '''
    Recebe um número inteiro e uma matriz de inteiros, e retorna a frequência do número na matriz.
    int, list(list) -> int
    '''
    freq = 0
    for i in matriz:
        for j in i:
            if numero == j:
                freq = freq + 1
    return freq