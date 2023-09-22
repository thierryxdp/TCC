def repetidos(n):
	'''Retorna quantas vezes o elemento da lista
	é igual ao elemento anterior.
	list -> int'''
	acc = 0
    i = 0
    while i < len(n):
        if i - 1 >= 0:
            if n[i] == n[i - 1]:
                acc += 1
        i += 1
    return acc