def filtraMultiplos (lista,n):
    """
    	Função que que retorna todos os numeros da lista 
        dada que são divididos pelo número dado.
    	lista,int -> lista
    """
    divisiveis = []
    a = 0
    proximo = lista[a]
    while proximo in lista:
        if proximo%n == 0:
            divisiveis = divisiveis + [proximo]
        a = a+1
        
    return divisiveis