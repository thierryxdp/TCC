def busca(setor, matriz):
    encontrados = []
    for funcionario in matriz:
        if setor in funcionario[2]:
            encontrados.append(funcionario[:2]+funcionario[3:])
	return encontrados