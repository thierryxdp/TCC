def conta_numero(numero,matriz):
    '''
    Função que dado um número inteiro e uma matriz de inteiros
    de tamanho qualquer, conta e retorna quantas vezes o
    número aparece na matriz.
    
    int, list -> int
    '''
    vezes = 0
    for linha in matriz:
        vezes = vezes + linha.count(numero)
    return vezes