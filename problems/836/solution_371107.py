def busca(matriz, setor):
    func = []
    for linha in matriz:
        for elemento in linha:
            if elemento == setor:
                func.append(linha)
	return func