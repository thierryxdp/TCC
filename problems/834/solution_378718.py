def media_matriz(matriz):
    lista=[]
    for i in matriz:
        for j in i:
            lista.append(j)
    colunas=len(matriz[0])
    linhas = len(matriz)
    relacao = linhas * colunas
    return round(sum(lista)/relacao,2)