def melhor_volta(matriz):
    ''' '''
    for i in matriz:
        for j in i:
            competidor=list.index(matriz,min(matriz))
            tempo=min(matriz[list.index(matriz,min(matriz))])
            volta=(list.index(lista,min(lista)))+1
    return (competidor,tempo,volta)