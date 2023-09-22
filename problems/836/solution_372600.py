def busca(setor,matriz):
    """dada uma matriz contendo os dados de funcionários de uma empresa, e um setor, a função retorna
    os dados de todos os funcionários daquele setor;
    str,list(list)->list"""
    linha=len(matriz)
    for i in range(linha):
        lista=[]
        if setor in matriz[i]:
            list.append(lista,matriz[i])
            list.remove(lista,setor)
    return lista