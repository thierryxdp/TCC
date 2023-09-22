#Exercício_03:
''' Essa função calcula a média dos números de uma matriz. '''
''' list ---> float. '''

def media_matriz(matriz):
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    ntotal = nlin*ncol
    
    list_soma = []
    
    for i in range(nlin):
        for j in range(ncol):
            list_soma += [matriz[i][j],]
    
    soma = sum(list_soma)
    
    media = soma/ntotal
    
    return float(round(media, 2)