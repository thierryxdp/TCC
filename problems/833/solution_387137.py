def conta_numero(numero,matriz):
    '''Funcao que recebe um numero inteiro e uma matriz de inteiros e conta
    quantas vezes o tal numero aparece na matriz.
    int, list(list(int)) -> int'''
    quantidade = 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade