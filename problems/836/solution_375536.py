def busca(setor,matriz):
    while range(len(matriz)) != 0:
        for aij in linha:
            if str(aij) == setor:
                return linha
        else:
            return []