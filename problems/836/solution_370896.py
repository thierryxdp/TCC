def busca(procurado,matriz):
    lista=[]
    for i in matriz:
        if procurado in i:
            lista= i
    return lista