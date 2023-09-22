def maiores(lista_numero,n):
    """ Função que dada uma lista de números inteiros e um número inteiro n, retorna uma lista alternativa, que contem todos os números da lista de origem maiores que n, em ordem crescente"""
    """int->list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    num = list.index(lista_numero,n)
    lista = lista_numero[num+1:]
	return lista