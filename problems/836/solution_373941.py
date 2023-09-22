def busca(setor,matriz):
    a=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            modif=matriz[i].pop(2)
            a+=[modif]
            
    return a