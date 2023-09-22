def maiores(lista, n):
    lista.append(n)
    list.sort(lista)
    indice = lista.index(n)
   	return lista[indice+1:]