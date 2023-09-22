def conta_numero(numero, matriz):
    '''Função que dada uma matriz de inteiros e um número inteiro, retorna quantas vezes aquele número aparece na matriz. '''
    conta=0
    for linha in matriz:
        conta += linha.count(numero)
    return conta