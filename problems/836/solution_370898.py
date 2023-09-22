def busca(procurado,matriz):
    lista=[]
    for i in matriz:
        if procurado in i:
            lista= [i[0]]+[i[1]]+[i[3]]+lista
    return lista