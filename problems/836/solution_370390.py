def busca(setor, matriz):
    resposta = []
    for linha in matriz:
        if setor in linha[2]:
            list.append(resposta, linha)
            list.remove(resposta, setor)
    return resposta