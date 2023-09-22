def busca(setor, m):
    registro = []
    for i in m:
        if i[2] == setor:
            del i[2]
            registro.append(i)
	return registro