def maiores(lista,n):
    """ Função que dada uma lista de números interiros e um numero inteiro n,retorna outra lista,
    que contenha todos os numeros da lista original maiores que n.
    lista -> list
    """
    lista_numeros = [lista]
	return [i for i in lista if i > n]
	lista_retorno = maiores(lista_numeros,n)
    lista_retorno.sort
    print(lista_retorno)