def busca(setor,matriz):
    '''recebe a string chamada setor, pertencente á matriz de strings, e retorna as sublistas que contém tal string dentro da matriz'''
    
    resposta = []
    for area in matriz:
        if area[2] == setor:
            list.append(resposta, area[:2] + area[3:])
    if resposta != []:
        return resposta
    return []