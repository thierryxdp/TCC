def melhor_volta(matriz):
    ''' '''
    for i in matriz:
        novalista=[]
        for j in i:
            list.append(novalista,j)
            tempo=min(novalista)
            competidor=(list.index(matriz,tempo))+1
            volta=(list.index(matriz,min(matriz)))+1
    return (competidor,tempo,volta)