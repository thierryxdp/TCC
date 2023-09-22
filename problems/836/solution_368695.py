def busca(setor,matriz):
    '''dado o nome de um setor da empresa, retorna uma lista com os dados de
    todos os funcionários daquele setor;
    str, list --> list'''
    lista = []
    for linha in matriz:
        if setor in linha[2]:
            list.remove(linha,linha[2])
            lista = lista + linha
    return lista