def filtra_pares(tupla):
    
    novaTupla = ()
    
    if (not(tupla[0] % 2)):
        novaTupla = novaTupla + tupla[0]
 
	if (not(tupla[1] % 2)):
        novaTupla = novaTupla + tupla[1]

    if (not(tupla[2] % 2)):
        novaTupla = novaTupla + tupla[2]

    if (not(tupla[3] % 2)):
        novaTupla = novaTupla + tupla[3]

    return novaTupla