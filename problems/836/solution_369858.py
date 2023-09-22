def busca(matriz, setor):
    ''' função que recebe uma string com o setor e uma matriz com as informações dos funcionários da empresa, e retorna os dados de todos os funcionários daquele setor;
    str, list -> list '''
    dados = []
    for x in matriz:
        if x[2] == setor:
            list.append(dados, x[:2] + x[3:])
    if dados != []:
        return dados
    return []