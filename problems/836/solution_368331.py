def busca(setor, matriz):
    '''Retorna uma lista contendo os dados de todos os funcionarios que trabalham no setor procurado'''
    #str, list -> list
    lista = []
    for linha in matriz:
        for Aij in linha:
            if Aij == setor:
                list.append(lista, linha)
                del(lista[:][2])
    return lista