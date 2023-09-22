def filtraMultiplos (lista,n):
    """
    	Função que que retorna todos os numeros da lista 
        dada que são divididos pelo número dado.
    	lista,int -> lista
    """
    divisiveis = []
    proximo = lista[0]
    while proximo in lista:
        if proximo%n == 0:
            divisiveis = divisiveis + [proximo]
        proximo = lista [0+1]
    return divisiveis