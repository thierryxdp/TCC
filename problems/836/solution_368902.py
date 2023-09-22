def busca(setor,matriz):
    "retorna as sublistas que a partir da matriz de strings e de uma string dentro dela"
    resposta = []
    for funca in matriz:
        if funca[2] == setor:
            list.append(resposta, funca[:2] + funca[3:])
    if resposta != []:
        return resposta
    return []