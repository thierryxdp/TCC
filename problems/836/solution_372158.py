def busca(setor,matriz): 
    retorno=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(retorno,matriz[i]) 
            list.remove(retorno,setor)
    return retorno