def conta_numero(numero, matriz):
    """Dado como entrada um número inteiro
    e uma matriz de números inteiros retorna
    quantas vezes aquele número aparece na matriz."""
    indice = 0
    while indice < len(matriz):
        if numero in matriz:
        	qtd = list.count(matriz,numero)
        indice += 1
        qtd += qtd
    return qtd