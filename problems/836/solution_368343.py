def busca(setor,matriz):
    '''Função que recebe uma string chamada setor, que é parte da matriz de
    strings, e retorna as sublistas que contém tal string dentro da matriz.'''
    resposta = []
    for funca in matriz:
        if funca[2] == setor:
            list.append(resposta, funca[:2] + funca[3:])
    if resposta != []:
        return resposta
    return []