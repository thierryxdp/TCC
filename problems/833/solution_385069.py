def conta_numero(numero, matriz):
    """Função que dado um número inteiro e uma matriz de inteiros retorna quantas vezes dito número aparece na matriz.
    int, list --> int"""
    contador = 0
    for lista in range(len(matriz)):
        contador = contador + list.count(matriz[lista], numero)
    return contador