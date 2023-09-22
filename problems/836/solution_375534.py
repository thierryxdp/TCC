def busca(setor,matriz):
    for linha in matriz:
        for aij in linha:
            if str(aij) == setor:
                return linha
        else:
            return []