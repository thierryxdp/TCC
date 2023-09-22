def filtraMultiplos(lista,numero):
	'''
	->'''
	retorno=[]
	contador=0
	quantidade_numero=len(lista)
	while (quantidade_numero>contador):
		if lista[contador]%numero==0:
			list.append(retorno,lista[contador])
		contador=contador+1
	return retorno