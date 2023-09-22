def busca(procurado,matriz):
    lista=[]
    for i in matriz:
        if procurado in i:
            k=i.remove(i[2])
            lista=k
    return lista