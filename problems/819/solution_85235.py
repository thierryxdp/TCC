#dado uma lista de números inteiros e um número n, verifica quais números são multiplos de n na lista e retorna-os em uma nova lista
#list->list
def filtraMultiplos(ls,n):
	lista=[]
	for x in ls:
		if x%n==0:
			lista.append(x)
	return lista