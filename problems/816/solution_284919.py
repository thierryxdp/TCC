def maiores(lista_nume,n):
	''' Essa função recebe uma lista de numero  e um numero inteiro,
   retornando outra lista e retorna todos os numeros maiores que o numero
   inteiro informado'''
    if n in lista_nume:
    	list.sort(lista_nume)
        lista= lista[list.index(lista_nume,n)+1:]
        return lista
    else:
        lista_nume.insert(-1,n)
        list.sort(lista_nume)
        lista= lista_nume[list.index(lista_nume,n)+1:]
        return lista