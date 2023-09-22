def conta_numero(numero, matriz):
    """Dado como entrada um número inteiro
    e uma matriz de números inteiros retorna
    quantas vezes aquele número aparece na matriz."""
    qtd = 0
    linhas = len(matriz)
    for i in range(linha):
        if numero in matriz[i]:
            qtd += matriz[i].count(numero)
        elif linhas == 0:
            return 0
        else:
            pass
    return qtd