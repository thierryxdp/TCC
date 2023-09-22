def filtra_pares (tup):
	'''Função que retorna uma nova tupla apenas com os elementos pares da original
tuple->tuple'''
	pares=()
	if (tup[0]%2)==0:
    	pares+=(tup[0],)
	if (tup[1]%2==0):
    	pares+=(tup[1],)
    if (tup[2]%2==0):
        pares+=(tup[2],)
    if (tup[3]%2==0):
        pares+=(tup[3],)
    return pares