def busca(setor, matriz):
	ret = []
	for arr in matriz:
		if setor in arr:
			ret.append([arr[0], arr[1], arr[3]])
	return ret