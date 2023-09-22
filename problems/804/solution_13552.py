#Filtra uma tupla com 4 elementos e retorma os pares
# tuple -> tuple
def filtra_pares(t):
    final = ()
	if t[0] % 2 == 0:
    	final += (t[0],)

	if t[1] % 2 == 0:
    	final += (t[1],)

	if t[2] % 2 == 0:
    	final += (t[2],)

	if t[3] % 2 == 0:
    	final += (t[3],)
	return final