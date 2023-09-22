def filtra_pares(p):
#dado uma tupla com 4 número inteiros retorna quais valores são pares em suas ordens originais
#tupla-->tupla
	a=p[0]
	b=p[1]
	c=p[2]
	d=p[3]
	lista = []
	if a%2>0 and b%2>0 and c%2>0 and d%2>0:
    	return 
	if a%2 == 0:
        lista.append(a)
    if b%2 == 0:
        lista.append(b)
    if c%2 == 0:
        lista.append(c)
    if d%2 == 0:
        lista.append(d)
		
	return(tuple(lista))