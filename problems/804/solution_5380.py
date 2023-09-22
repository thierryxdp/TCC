def filtra_pares(a):
    saida = ()
    for i in range(4):
    	if a[i]%2 == 0:
            saida = saida + (a[i],)
    return saida