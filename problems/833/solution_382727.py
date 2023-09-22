def conta_numero(numero,matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    qtd_n = []
    
    for linhas in matriz:
        for colunas in linhas:
            qtd_n += [str.count(str(matriz),str(numero))]
    return len(qtd_n)