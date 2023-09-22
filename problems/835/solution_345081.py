def melhor_volta(matriz):
    ''' '''
    for i in matriz:
        
        for j in i:
            tempo=min(matriz[list.index(matriz,min(matriz))])
            competidor=(list.index(matriz,tempo))+1
            volta=(list.index(matriz,min(matriz)))+1
    return (competidor,tempo,volta)