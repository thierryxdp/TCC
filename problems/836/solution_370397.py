def busca(setor, matriz):
    resposta = []
    lista_setor = []
    for linha in matriz:
        if setor in linha:
            list.append(lista_setor, linha)
            for lista in lista_setor:
                list.pop(lista, 2)
                list.append(resposta, lista)
    return resposta