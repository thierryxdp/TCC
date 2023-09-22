def insere(lista_numero,n):
    """Inclui um número em sua posição correta em uma lista ordenada
    	list, int -> list
        Parameters:
        lista_numero: Lista ordenada de números inteiros
        n: Número inteiro
        
        Returns:
        Lista ordenada de números inteiros com n na posição correta
    """
    
    list.append(lista_numero,n)
    list.sort(lista_numero)
    
    return lista_numero