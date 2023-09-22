def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            del matriz[i][2]
            list.append(lista, matriz[i])
        i+=1
        return lista