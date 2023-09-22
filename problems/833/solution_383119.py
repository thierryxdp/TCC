def conta_numero(numero, matriz):
    """Dado como entrada um número inteiro
    e uma matriz de números inteiros retorna
    quantas vezes aquele número aparece na matriz."""
    indice = 0
    qtd = 0
    while indice < len(matriz):
        if numero in matriz[indice]:
            qtd = list.count(matriz,numero)
            qtd += qtd
        indice += 1
    return qtd