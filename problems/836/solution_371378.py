def busca(setor,matriz):
    lista=[]
    for i in matriz:
        for j in i:
            if setor in j:
                lista.append(i[0],i[2],i[3])
    return lista