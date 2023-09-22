def busca(buscasetor,matriz):
    lista=[]
    for infos in matriz:
        if str.lower(buscasetor)==str.lower(infos[2]):
            list.append(lista,[infos[0],infos[1],infos[3]])
    return lista