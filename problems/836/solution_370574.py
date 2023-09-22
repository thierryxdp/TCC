def busca(setor, matriz):
    lista = []
    for i in matriz:
        if setor in i:
            lista.append(i)
    return lista