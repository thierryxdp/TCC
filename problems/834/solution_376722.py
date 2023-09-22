def media_matriz(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de entrada, retorna quantas vezes esse número aparece na matriz'''
    soma = 0
    for n in range(len(matriz)):
        soma += list.count(matriz[n],numero)
    return soma