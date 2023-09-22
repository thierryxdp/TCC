def faltante(lista):
    """Dá o número de uma peça faltante de uma lista
    	list -> int
        Pameters:
        lista: Lista com número das peças
        
        Returns:
        Número da peça faltante da lista
    """
    
    i = 1
    
    while i < len(lista):
        if i not in lista:
            return i
        else:
            i = i+1