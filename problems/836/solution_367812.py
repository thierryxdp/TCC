def busca(setor,matriz):
    lista = []
    for i in matriz:
        for j in i:
            if j == setor:
                lista.append(i)
    return lista