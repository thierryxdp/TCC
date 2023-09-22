def maiores(lista,n):
    """ Função que dada uma lista de números interiros e um numero inteiro n,retorna outra lista,
    que contenha todos os numeros da lista original maiores que n.
    lista -> list
    """
  		for elemento in lista:
    	if elemento > n:
        	lista_final.append(elemento)

	print(lista_final)