def busca(setor, matriz):
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)
    setor_1 = lista.index(setor)
    lista_1 = lista[setor_1 - 2 : setor_1 + 2]
    return lista_1