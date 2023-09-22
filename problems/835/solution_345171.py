def melhor_volta(matriz):
    ''' '''
    novalista=[]
    for i in matriz:
        for j in i:
            list.append(novalista,j)
            tempo=min(novalista)
            competidor=list.index(matriz,min(matriz))
            volta=((list.index(novalista,tempo))+1)//competidor
    return (competidor,tempo,volta)