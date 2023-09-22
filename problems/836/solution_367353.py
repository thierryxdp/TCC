def busca(setor,matriz):
    lista=[]
    i=0
    for linha in matriz:
        if linha[2]==setor:
            list.append(lista,linha)
            list.remove(lista[i],setor)
            i+=1
    return lista