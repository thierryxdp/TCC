def melhor_volta(matriz):
    ''' '''
    novalista=[]
    for i in matriz:
        for j in i:
            list.append(novalista,j)
            tempo=min(novalista)
            competidor=((novalista.index(min(novalista)))//6)+1
            volta=(list.index(matriz,min(matriz)))+1
    return (competidor,tempo,volta)