def busca(setor, matriz):
    func = []
    for linha in matriz:
        for elemento in linha:
            if elemento == setor:
                func.append(linha.remove(setor))
                
	return func