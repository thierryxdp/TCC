def conta_numero(numero,matriz):
    """Dada uma matriz e um número qualquer como entrada,
    retorna quantas vezes esse número aparece na matrizes; int, list -> int"""
    coluna = len(matriz[0])
    linha = len(matriz)
    qtd = 0 
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == numero:
                    qtd = qtd+1
        return qtd