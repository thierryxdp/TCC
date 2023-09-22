def busca(setor,matriz):
    '''função que dado um nome de um setor de uma empresa, retorna os dados
    de todos os funcionários daquele setor; str, list(list) -> list(list)'''
    nomes = []
    for linha in matriz:
        if setor in linha:
            del linha[2]
            nomes = nomes + [linha]
    return nomes