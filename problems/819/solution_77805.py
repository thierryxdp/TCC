def filtraMultiplos(lista, n):
    """função que recebe uma lista e um número(n) e retorna outra lista contendo 
	os elementos que forem divisíveis por n
	list, int -> list"""
    
    listan = ()
    i = 0
    
    while i < len(lista):
        if int(lista[i])%n == 0:
            listan = listan + (lista[i],)
        i = i + 1
	return list(listan)