def conta_numero (numero, matriz):
    """Funcao que dado um numero inteiro e uma matriz de inteiros conta e retorna quantas vezes aquele numero aparece na matriz"""
    qtd = 0
    linhas = len(matriz)
    for i in range(linhas):
        if numero in matriz[i]:
            qtd += matriz[i].count(numero)
        elif linhas == 0:
            return 0
        else:
            pass
    return qtd