def conta_numero(numero,matriz):
    '''Função que dada uma matriz de inteiros e um numero inteiro, retorna quantas vezes
    esse numero aparece na matriz. int, list -> int'''
    soma = 0
    for n in range(len(matriz)):
        soma += list.count(matriz[n],numero)
    return soma