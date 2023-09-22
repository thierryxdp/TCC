def busca(setor, matriz):
    lista = []
    for i in matriz:
        if setor in i:
            lista.append(i)
            lista.pop(i[2])
    return lista