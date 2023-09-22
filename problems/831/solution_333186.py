def lingua_p(p):
    r = ''
    for i in p:
		if i.lower() in 'aeiouáéíóúã':
            r += i + 'p' + i
        else:
            r += i
	return r