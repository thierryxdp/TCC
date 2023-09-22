#Filtra uma tupla com 4 elementos e retorma os pares
# tuple -> tuple
def filtra_pares(t):
    a, b, c, d = t
    final = ()
	if a % 2 == 0:
    	final = a,

	if b % 2 == 0:
    	final = b,

	if c % 2 == 0:
    	final = c,

	if d % 2 == 0:
    	final = d,
	return final