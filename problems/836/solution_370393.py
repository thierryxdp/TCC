def busca(setor, matriz):
    resposta = []
    for linha in matriz:
        if setor in linha[2]:
            list.append(resposta, linha)
        for lista in resposta:
            list.pop(lista, 2)
    return resposta