def maiores(lista, n):
    """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maior que n
    """
    nova_lista = lista[:]
    nova_lista =  for elem in lista if elem > n
    
    return nova_lista