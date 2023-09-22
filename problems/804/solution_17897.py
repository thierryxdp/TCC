def filtra_pares(tupla):
	tupla_filt = tuple()

	if (tupla[0]%2) == 0:
        tupla_filt = tupla_filt + (tupla[0],)
        
	if (tupla[1]%2) == 0:
        tupla_filt = tupla_filt + (tupla[1],)
        
    if (tupla[2]%2) == 0:
        tupla_filt == tupla_filt + (tupla[2],)
        
    if (tupla[3]%2) == 0:
        tupla_filt == tupla_filt + (tupla[3],)
        
    return tupla_filt