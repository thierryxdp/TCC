def busca(setor,matriz):
    """dada uma matriz contendo os dados de funcionários de uma empresa, e um setor, a função retorna
    os dados de todos os funcionários daquele setor;
    str,list(list)->list"""
    linha=len(matriz)
    coluna=len(matriz[0])
    lista=[]
    for i in range(linha):
        if setor in matriz[i]:
            list.append(lista,matriz[i])
    return lista