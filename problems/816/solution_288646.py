def maiores(lista_numero,n):
    """Determinar uma lista crescente com todos os numeros maiores que n;
    list, int - > list"""
    lista_numero += [n,]
    lista_numero.sort()
    indice = lista_numero.index👎
    lista = lista_numero[indice+1:]
    	return lista