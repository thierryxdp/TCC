def busca(setor,matriz):
    lista = []
    for i in matriz:
        if setor in matriz[i]:
            lista = lista + matriz[i]
    return lista