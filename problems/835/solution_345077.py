def melhor_volta(matriz):
    ''' '''
    competidor=list.index(matriz,min(matriz))
    tempo=min(matriz[list.index(matriz,min(matriz))])
    volta=(list.index(matriz,min(matriz)))+1
    for i in matriz:
        for j in i:
    return (competidor,tempo,volta)