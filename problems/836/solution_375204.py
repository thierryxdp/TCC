def busca(busca_setor,matriz):
    '''Função que recebe uma matriz e que faz uma busca por setor;
    str,list->list'''
    lista=[]
    for infos in matriz:
        if str.lower(busca_setor)==str.lower(infos[2]):
            list.append(lista,[infos[0],infos[1],infos[3]])
    return lista