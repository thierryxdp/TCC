def lingua_p(pal):
    aux=''
    for i in range(pal):
        if str.lower(pal[i]) in 'aeiouáéíóúàèìòùãõ':
            aux = aux + pal[i] + 'p' + pal[i]
        else:
            aux = aux + pal[i]
	return str.lower(aux)