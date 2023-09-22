def melhor_volta(matriz):
    ''' '''
    novalista=[]
    menores=[]
    for i in matriz:
        for j in i:
            list.append(novalista,j)
            tempo=min(novalista)
            competidor=novalista.index(tempo)//6
            volta=novalista.index(tempo)+1//10
    return (competidor,tempo,volta)