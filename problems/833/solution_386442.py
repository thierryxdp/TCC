def conta_numero(numero,matriz):
    '''Função que, dada uma matriz e um número inteiro como valores de entrada, retorna quantas vezes tal numero aparece na matriz; int, list[list] -> int'''
    vezes=0
    for linha in matriz:
        vezes+=list.count(linha,numero)
    return vezes