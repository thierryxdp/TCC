def filtra_pares(tupla):
    
    novaTupla = ()
    
    if (not(tupla[0] % 2)):
        novaTupla = (tupla,)
 
	if (not(tupla[1] % 2)):
        novaTupla = (tupla,)

    if (not(tupla[2] % 2)):
        novaTupla = (tupla,)

    if (not(tupla[3] % 2)):
        novaTupla = (tupla,)

    return novaTupla