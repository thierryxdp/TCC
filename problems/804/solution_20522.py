def filtragem(a):
    pares_novos=()
    if a[0]%2==0:
        pares_novos=pares_novos+(a[0],)
    if a[1]%2==0:
        pares_novos=pares_novos+(a[1],)
	if a[2]%2==0:
        pares_novos=pares_novos+(a[2],)
	if a[3]%2==0:
        pares_novos=pares_novos+(a[3],)
	return pares_novos