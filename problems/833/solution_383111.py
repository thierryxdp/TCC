def conta_numero(numero, matriz):
    """Dado como entrada um número inteiro
    e uma matriz de números inteiros retorna
    quantas vezes aquele número aparece na matriz."""
    indice = 0
    while indice < len(matriz):
        if numero in matriz:
            qtd = 0
        	qtd = list.count(matriz,numero)
        indice += 1
    return qtd