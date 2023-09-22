def busca(string, matriz):
    '''Função que busca por setor a fim de retornar uma lista
    com os dados de todos os funcionários daquele setor.
    str, list(list)'''
    buscaFeita=[]
    for linha in matriz:
            if linha[2]==string:
                buscaFeita.append(range(matriz[linha][0:2]),linha[3:]) 
                return buscaFeita
    return buscaFeita