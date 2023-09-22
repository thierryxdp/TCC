def busca(setor,matriz):
    '''Dado o nome do setor da empresa, retorna os dados de todos os funcionários
    do setor.
    str, list -> list'''
    busca = []
    for pessoa in matriz:
        if setor in pessoa[2]:
            del pessoa[2]
            list.append(busca,pessoa)

    return busca