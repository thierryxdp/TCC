def busca(setor,matriz):
    """dada uma matriz contendo os dados de funcionários de uma empresa, e um setor, a função retorna
    os dados de todos os funcionários daquele setor;
    str,list(list)->list"""
    linha=len(matriz)
    lista=[]
    for i in range(linha):
        if setor in matriz[i]:
            list.append(lista,matriz[i])
            list.del(lista,list.index(lista,setor))
    return lista