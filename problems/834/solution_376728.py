def media_matriz(matriz):
    l = range(len(matriz))
    c = range(len(matriz[0]))
    soma_termos = 0
    parcela = []
    
    for i in l:
        for j in c:
            parcela+=[matriz[i][j]]
    soma_termos = sum(parcela)
    media =  soma_termos/(len(matriz)*len(matriz[0]))
    
    return round(media,2)