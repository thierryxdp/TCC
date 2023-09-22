def eh_quadrada(m):
    """Função que recebe uma matriz e retorna se é quadrada ou n"""
    i = 0
    if m == []:
        return True
    while i < len(m):
        l = m[i]
        if len(m) == len(l):
            r = True
		if len(m) != len(l):
            r = False
		i = i+1
	return type(m)