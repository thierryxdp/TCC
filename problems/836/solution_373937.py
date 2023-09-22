def busca(setor,matriz):
    a=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            a+=[matriz[i]]
            
    return a