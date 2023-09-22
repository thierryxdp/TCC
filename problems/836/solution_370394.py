def busca(setor, matriz):
    resposta = []
    lista_setor = []
    for linha in matriz:
        if setor in linha[2]:
            list.append(lista_setor, linha)
            for lista in lista_setor:
                list.remove(lista, setor)
                list.append(resposta, lista)
    return resposta