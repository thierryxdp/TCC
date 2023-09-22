def busca(setor,matriz):
    '''recebe uma matriz e faça uma busca por setor, ou seja, dado um nome de um setor da empresa, a funçao retorna os dados de todos funcionários daquele setor'''
    '''list(list(str)) -> list(str)'''
    resposta = []
    for funcao in matriz:
        if funcao[2] == setor:
            list.append(resposta, funcao[:2] + funcao[3:])
    if resposta != []:
        return resposta
    return []