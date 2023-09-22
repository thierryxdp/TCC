def busca(buscasetor,matriz):
    lista=[]
    for infos in matriz:
        for setor in matriz[infos]:
            if str.lower(buscasetor) in str.lower(setor):
                list.append(lista,[infos[0],infos[2],infos[3]])
    return lista