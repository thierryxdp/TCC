def maiores(lista_numero,n):
	"""Dado uma lista de números inteiros e um número n, retorna a lista
	em ordem crescente à partir dos números maiores que n:
	list,int-->list"""
    lista_numero=lista_numero+[n]
    lista_numero.sort()
    del lista_numero[0:lista_numero.index(n)]
    lista_numero.remove(n)
    return lista_numero