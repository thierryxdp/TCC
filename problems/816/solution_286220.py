def maiores(lista_numeros,n):
	lista=lista_numeros+[n]
    list.sort(lista)
  	lista=list.remove(lista,n)
    return lista