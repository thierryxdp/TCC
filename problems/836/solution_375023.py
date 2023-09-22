def busca(string, matriz):
    '''Função que busca por setor a fim de retornar uma lista
    com os dados de todos os funcionários daquele setor.
    str, list(list)'''
    buscaFeita=[]
    for linha in range(len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if matriz[linha][coluna]==string:
                buscaFeita= list.append(buscaFeita, linha[0:2], linha[3:]) 
                return buscaFeita
            else:
                return buscaFeita