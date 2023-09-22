def busca(setor,matriz):
    '''funçao que busca o funcionário na matrizc com base no setor''' 
    '''str,list[str]->list[str]'''
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista,matriz[i]) 
    for g in range(len(lista)):
        indice=list.index(lista[g],setor)
        list.pop(lista[g],indice)
    return lista