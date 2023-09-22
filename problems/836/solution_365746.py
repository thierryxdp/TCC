def busca(setor,matriz):
    '''Função que recebe uma uma matriz e uma string chamado setor e retorna os dados de todos
    os funcionários daquele setor
    list(list(str)) -> list(str)'''
    resposta = []
    for funca in matriz:
        if funca[2] == setor:
            list.append(resposta, funca[:2] + funca[3:])
    if resposta != []:
        return resposta
    return []