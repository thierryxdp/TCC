def filtra_pares(n0,n1,n2,n3):
	tupla= (n0,n1,n2,n3)
	if tupla[0]/2==int and tupla[1]/2==int and tupla[2]/2==int and tupla[3]/2==int:
        return tupla
    elif tupla[0]/2!=int and tupla[0]/2==int and tupla[2]/2==int and tupla [3]/2==int:
        return tupla[1:]