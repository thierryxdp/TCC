def busca(procurado,matriz):
    lista=[]
    for i in matriz:
        if procurado in i:
            i.remove(i[2])
            lista=[i+lista]
    return lista