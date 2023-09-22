'''função que recebe uma lista e um número e o inclui na lista de forma ordenada.
	list,int -> list'''
def insere(lista_numero,n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero