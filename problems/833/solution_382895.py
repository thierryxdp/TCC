def conta_numero(n, matriz):
    '''Função que dado um número inteiro e uma matriz de entrada, retorna quantas vezes esse número aparece na matriz'''
    soma = 0
    for x in range(len(matriz)):
        soma += list.count(matriz[x],numero)
    return soma