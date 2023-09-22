def maiores(lista, n):

    """ Se quisermos, numa ocasião, escolher apenas números numa lista
        maiores que um valor n, isto é possível com esta função.
        Ela retornará apenas valores maiores que o valor n dado em comparação
        com uma lista também dada.

        list,int -> list
    """
	
	
    numeros = []
    i=0
	
    while i < len(lista):
        if lista[i] > n:
            list.append(numeros,lista[i])
        i=i+1
    return sorted(numeros)