def busca(procurado,matriz):
    lista=[]
    for i in matriz:
        if procurado in i:
            lista=list.remove(i,i[2])
    return lista