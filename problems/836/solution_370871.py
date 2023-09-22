def busca(setor,matriz):
    lista=[]
    
    for i in matriz:
        if i[2]==setor:
            i.remove(setor)
            lista.append(i)
    return lista