def busca(setor,matriz):
    a=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            modif=matriz[i].remove(setor)
            a+=[modif]
            
    return a