def busca (matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista,matriz[i])
    for g in range(len(lista)):
        indice=list.index(lista[g],setor)
        list.pop(lista[g],indice)
    return lista