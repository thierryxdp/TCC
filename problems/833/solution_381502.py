def conta_numero(numero,matriz):
    linhas=len(matriz)
    colunas=len(matriz[0])
    qtd=0
    for numero in range(linhas):
        qtd=qtd+1
        for num in range(colunas):
            if num==numero:
                qtd=qtd+1
    return qtd