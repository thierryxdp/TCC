def busca(setor,matriz):
    lista=[]
    for e in matriz:
        if setor in e:
            ef=e[:]
            eff=ef.remove(setor)
            list.append(lista,eff)
    return lista