def  busca(setor,matriz):
    lista=[]
    for i in matriz:
        for k in i:
            if k==setor:
                lista.append(i)
                return lista