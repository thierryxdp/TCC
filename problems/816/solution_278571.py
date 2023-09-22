def maiores(lista,n):
    """Retorna os números de uma lista maiores que n
    	list, int -> list
        Parameters:
        lista: Lista de números inteiros
        n: Número inteiro
        
        Return:
        A lista fornecida somente a partir do número n definido
    """
    
	list.append(lista,n)
    ordenada = list.sort(lista)
    indice = list.index(ordenada,n)
    
    if n not in ordenada:
        list.append(lista,n)
        
    return ordenada[indice+1:]