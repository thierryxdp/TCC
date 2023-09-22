def busca(setor, matriz):
    """ Função que recebe uma matriz contendo os dados
    dos funcionários e um setor da empresa, realiza uma busca
    e retorna os dados de todos os funcionários daquele setor
    list -> list"""
    lista_dados = []
    for i in matriz:
        if i[2] == setor:
            list.append(lista_dados, i[:2] + i[3:])
    if lista_dados != []:
        return lista_dados
    return []