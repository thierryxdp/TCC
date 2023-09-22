def media_matriz(matriz):
    """função que retorna a média de todos os 
    números de uma dada matriz
    list=>float"""
    lista=[]
    for i in matriz:
        for j in i:
            lista.append(j)
    colunas=len(matriz[0])
    linhas = len(matriz)
    relacao = linhas * colunas
    return round(sum(lista)/relacao,2)