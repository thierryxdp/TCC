def busca(setor,matriz):
    lista=[]
    for i in matriz:
        for j in i:
            if setor in j:
                lista.append(j)
    return lista