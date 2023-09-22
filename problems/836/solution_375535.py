def busca(setor,matriz):
    while linha in matriz:
        for aij in linha:
            if str(aij) == setor:
                return linha
        else:
            return []