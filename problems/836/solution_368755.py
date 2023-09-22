def busca(matriz, setor):
    encontrados = []
    for funcionario in matriz:
        if setor in funcionario:
            encontrados.append(funcionario[:2]+funcionario[3:])
	return encontrados