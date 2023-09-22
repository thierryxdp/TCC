def busca(setor, matriz):
    ''' Dado um setor da empresa, a função retorna os dados de todos os
        funcionarios do mesmo setor
        str, list -> list'''
    lista = []
    for i in matriz:
        if setor in i:
            i.remove(setor)
            list.append(lista, i)
    return lista