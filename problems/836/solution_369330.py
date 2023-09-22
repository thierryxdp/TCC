def busca(setor, matriz):
    lista = []
    for x in matriz:
        if x[2] == setor:
            del(x, 2)
            lista.append(x)
    return lista