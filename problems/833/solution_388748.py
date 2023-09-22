def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho qualquer,
conta e retorna quantas vezes aquele número aparece na matriz.
float, list(list)->int'''
    total=0
    for linha in matriz:
        total+=list.count(linha,numero)
    return total