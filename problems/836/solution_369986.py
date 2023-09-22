def busca(setor,matriz):
    """Dado o nome do setor da empresa e a matriz com os dados dos funcionários,
    retorna os dados de todos os funcionários daquele setor;str,list->list"""
    setor=str.lower(setor)
    lista=[]
    for i in range(len(matriz)):
        if str.lower(matriz[i][2])==setor:
            list.append(lista,matriz[i])
    return lista