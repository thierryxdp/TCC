def media_matriz(matriz):
    'Dada uma matriz, retorna a média dos números da matriz. Entradas: list[list]. Saída: float.'
    linhas=len(matriz)
    colunas=len(matriz[0])
    qtd=0
    for l in range(linhas):
        for c in range(colunas):
            soma=soma+matriz[l][c]
            qtd=qtd+1
    media=round(soma/qtd,2)
    return media