def insere(lista_numero,n):

	'''
Forma uma nova lista com o numero inteiro dado em ordem crescente
Parâmetros: 
lista_numero: list.
	lista que o usuario informou
n: int
	numero inteiro que vai formar a nova lista
Returns: list
Nova lista em ordem crescente de acordo com o numero inteiro informado
	'''	
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero