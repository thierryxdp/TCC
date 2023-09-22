def busca(setor,matriz):
    retorno=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(retorno,matriz[i]) 
    for g in range(len(retorno)):
        if list.index(retorno[g],setor)==True:
            list.remove(retorno[g],setor)
    return retorno