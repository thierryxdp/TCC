def busca(setor,matriz):
    resposta = []
    for funca in matriz:
        if funca[2] == setor:
            list.append(resposta, funca[:2] + funca[3:])
    if resposta != []:
        return resposta
    return []