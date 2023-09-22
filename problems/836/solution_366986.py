def busca(setor,matriz):
    lista=[]
    i=0
    while i < len(matriz):
        if setor in matriz[i]:
            del matriz[i][2]
            list.append(lista, matriz[i])
            i+=1
        return lista