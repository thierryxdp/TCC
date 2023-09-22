def busca(setor,matriz):
    
    for i in matriz:
        for k in i[2]:
            if k==setor:
                lista=[]
                lista.append(i)
    return lista