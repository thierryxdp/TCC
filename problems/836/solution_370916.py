def busca(setor,matriz):
    func = []
    for linha in matriz:
        for elemento in linha:
            if elemento == setor:
                func.append(linha)
		func.remove(setor)
    return func