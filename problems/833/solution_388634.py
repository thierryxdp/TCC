def conta_numero(numero,matriz):
    '''funçao que dado um numero inteiro e uma matriz de inteiros
    de tamanho qualquer, conta e retorna quantas vezes aquele
    numero aparece na matriz'''
    x = 0
    for y in matriz:
        x = x+list.count(y,numero)
        return x