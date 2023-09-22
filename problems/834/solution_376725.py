def teste(matriz):
    lista = []
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            

def media_matriz(matriz):
    linha=range(len(matriz))
    coluna=range(len(matriz[0]))
    soma=0
    parcela=[]
    
    for i in linha:
        for j in coluna:
            parcela+=[matriz[i][j]]
    soma=sum(parcela)
    media=soma/(len(matriz)*len(matriz[0]))
    
    return round(media,2)