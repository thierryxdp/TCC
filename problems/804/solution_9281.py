def filtra_pares(tupla):
    '''
    tupla(int,int,int,int)-> tupla'''
    nova_tupla = ()
    for numero in tupla:
        if (numero % 2) == 0:
        	nova_tupla.index(numero)
	return nova_tupla