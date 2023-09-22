def busca(string, matriz):
    '''Função que busca por setor a fim de retornar uma lista
    com os dados de todos os funcionários daquele setor.
    str, list(list)'''
    busca_feita=[]
    for linha in range(len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if matriz[linha][coluna]==string:
                busca_feita= list.append(busca_feita,linha[0:2] + linha[3:])
                return busca_feita
            else:
                return busca_feita