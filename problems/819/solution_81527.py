def filtraMultiplos (lista,n):
    """
    	Função que que retorna todos os numeros da lista 
        dada que são divididos pelo número dado.
    	lista,int -> lista
    """
    divisiveis = []
    i = 0
    while i<len(lista):
        if proximo%n == 0:
            divisiveis = divisiveis + lista[i]
        i = i + 1
        
    return divisiveis