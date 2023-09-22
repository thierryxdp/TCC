def filtra_pares(n):
	"Essa função retorna os numeros pares de uma função"
	a =()
	if n[0] % 2 == 0:
        a = a + (n[0],)
    else:
        a = a
	if n[1] % 2 == 0:
        a = a + (n[1],)
    else:
        a = a
    if n[2] % 2 == 0:
    	a = a + (n[2],)
    else:
        a = a   
    if n[3] % 2 == 0:
        a = a + (n[3],)
    else:
        a = a
    return a