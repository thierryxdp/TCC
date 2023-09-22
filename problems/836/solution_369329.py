def busca(setor, matriz):
    lista = []
    for x in matriz:
        if x[2] == setor:
            lista.append(x)
    return lista