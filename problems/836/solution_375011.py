def busca(string, matriz):
    '''Função que busca por setor a fim de retornar uma lista
    com os dados de todos os funcionários daquele setor.
    str, list(list)'''
    busca_feita=[]
    for linha in matriz:
        if matriz[0][0]==string or string==matriz[1][0] or string==matriz[2][0]:
            return list.append(busca_feita,linha[0:2] + linha[3:])
        else:
            return busca_feita