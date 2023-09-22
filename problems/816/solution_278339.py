def maiores(lista,n):

    '''Forma uma nova lista com os numeros maiores do que o fornecido
Parâmetros: 
lista: list.
	lista que o usuario informou
n: int
	numero inteiro que vai deternimar a nova lista
Returns: list
Nova lista em ordem crescente de acordo com o numero inteiro informado
	'''  
   
	list.sort(lista)
    return lista[n:]