def filtra_pares(tupla):
     if tupla == ():
    	return 0
     else:
    	return tupla[0] + conta_pares(tupla[1:])