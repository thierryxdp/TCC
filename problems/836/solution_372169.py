def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista,matriz[i]) 
    for g in range(len(lista)):
        if list.index(lista[g],setor)==True:
            list.remove(lista[g],setor)
    return lista