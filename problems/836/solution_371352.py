def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista.append(matriz[i])
    for i in range(len(lista)):
        lista[i].remove(setor)
            
    return lista