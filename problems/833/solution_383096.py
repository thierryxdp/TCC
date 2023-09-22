def conta_numero(numero, matriz):
    """Dado como entrada um número inteiro
    e uma matriz de números inteiros retorna
    quantas vezes aquele número aparece na matriz."""
    if numero in matriz:
        qtd = list.count(matriz,numero)   
        return qtd