def repetidos(ls):
	new_ls = []
    repetidos = []
	for n in ls:
		if n in new_ls:
			repetidos.append(n)
		else:
			new_ls.append(n)
	return len(set(repetidos))