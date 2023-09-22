def conta_numero(numero,matriz):
    qtd_linhas=len(matriz)
    qtd_colunas=len(matriz[0])
    qtd_numeros=0
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if i and j == numero:
                qtd_numeros=numero
    return qtd_numeros