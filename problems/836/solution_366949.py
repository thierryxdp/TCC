def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        for setor in matriz[i][2]:
            i+=1
            lista+=[matriz[i]]
            del matriz[i][2]
        return perfil