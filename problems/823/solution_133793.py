def faltante(lista):
    
    """Fução que dada uma lista com N − 1 inteiros numerados de 1 a N, descubra qual n ́umero
	inteiro deste intervalo está faltando.
    list -> int"""
    
    list.sort(lista)
    
    conta_pecas = []
    i = 0
    acumulador = 1
    
    while i < len(lista):
        
        if lista[i] == acumulador:
            acumulador += 1
        
        i += 1
        
    return acumulador