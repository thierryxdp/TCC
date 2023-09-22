def busca(setor,matriz):
    retorno=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(retorno,matriz[i]) 
    for g in range(len(retorno)):
        indice=list.index(retorno[g],setor)
        list.remove(retorno[indice],setor) 
    return retorno