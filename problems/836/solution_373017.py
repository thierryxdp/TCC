def busca(setor,matriz):
    '''funcao que recebe uma matriz e faz uma busca por setor,
    ou seja, dado um nome de um setor da empresa, a funcao retorna
    os dados de todos os funcionarios daquele setor
    str,list->list'''
    lista_vazia=[]
    for linhas in matriz:
        for colunas in linhas:
            if setor in linhas:
                list.append(lista_vazia,linhas)
    return lista_vazia