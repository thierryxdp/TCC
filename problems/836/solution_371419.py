def busca(setor,matriz):
    """retona o nome doa funcioanrios de um setor a partir de uma matriz
    lista->lista"""
    resposta = []
    for funca in matriz:
        if funca[2] == setor:
            list.append(resposta, funca[:2] + funca[3:])
    if resposta != []:
        return resposta
    return []