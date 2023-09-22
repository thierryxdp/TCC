def busca(setor,matriz):
    g=0
    retorno=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(retorno,matriz[i]) 
    list.remove(retorno[0],setor)
    return retorno