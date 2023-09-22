def busca(string, matriz):
    '''Função que busca por setor a fim de retornar uma lista
    com os dados de todos os funcionários daquele setor.
    str, list(list)'''
    buscaFeita=[]
    for linha in matriz:
        for coluna in range(len(matriz[linha])):
            if linha[2]==string:
                buscaFeita.append(linha[0:2], linha[3:]) 
                return buscaFeita
            else:
                return buscaFeita