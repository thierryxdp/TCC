def conta_numero(numero:int,matriz:list)->int:
    """Dada uma matriz e um número inteiro n, retorna quantas vezes esse número aparece na matriz."""
    contagem_n=0
    for linha in range(len(matriz)):
        contagem_n+=list.count(matriz[linha],n)
    return contagem_n