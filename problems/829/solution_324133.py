def H(n):
    return 1/n

def soma_h(n):
    i=1
    lista_de_valores=[]
	while i<=n+1:
		if H(i) != H(n):
			list.append(lista_de_valores,H(i))
			i=i+1
		else:
			list.append(lista_de_valores,H(n))
			return round(sum(lista_de_valores),2)