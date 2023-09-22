def qtd_divisores(n):
    """ Função que conta o número de divisores.
    int, int->int """
	lista = []
	for x in range(1,n):
		if n%x==0:
			lista.append(x)
	return (sum(lista))