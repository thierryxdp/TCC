def faltante(l):
    '''Retorna o número faltante da lista.
    list -> int''''
    list.sort(l)
    i = 0
    while i < len(l):
        if l[0] > 1:
            return l[0] - 1
        elif i + 1 < len(l) and l[i + 1] - l[i] > 1:
        	return l[i] + 1
        i += 1
    return l[- 1] + 1