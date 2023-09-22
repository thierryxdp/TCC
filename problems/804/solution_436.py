def filtra_pares(a,b,c,d):
	'''Função que recebe quatro elementos inteiros como parâmetro e retorna uma nova tupla
	contendo apenas os elementos pares da tupla original, mantendo a ordem;
	Entrada: tupla
	Saída: tupla'''
	a2=float(a)%2
	b2=float(b)%2
	c2=float(c)%2
	d2=float(d)%2
	if a2+b2+c2+d2==0:
		return (a,b,c,d)
	elif a2==0 and b2==0 and c2==0 and d2!=0:
		return (a,b,c)
	elif a2==0 and b2==0 and c2!=0 and d2!=0:
		return (a,b)
	elif a2==0 and b2!=0 and c2==0 and d2!=0:
		return (a,c)
	elif a2==0 and b2!=0 and c2!=0 and d2==0:
		return (a,d)
	elif a2!=0 and b2==0 and c2==0 and d2!=0:
		return (b,c)
	elif a2==0 and b2!=0 and c2!=0 and d2!=0:
		return (a)
	elif a2!=0 and b2==0 and c2!=0 and d2!=0:
		return (b)
	elif a2!=0 and b2!=0 and c2==0 and d2!=0:
		return (c)
	elif a2!=0 and b2!=0 and c2!=0 and d2==0:
		return (d)