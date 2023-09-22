def busca(matriz, setor):
    encontrados = []
    for funcionario in matriz:
        if setor == funcionario[2]:
            encontrados.append(funcionario[:2]+funcionario[3:])
	return encontrados