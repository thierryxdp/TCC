def filtraMultiplos (lista, n):
    """ Dado uma lista de nmeros e um numero n, retorna uma nova lista contendo os numeros da lista inicial multiplos do numero n.
    entrada lista com numros inteiros, int -> saida lista de numeros inteiros. """
    i = 0
    multiplos = []
    
    while i < len(lista):
        if lista[i]%2 == 0:
            lista2 = lista[i]
            multiplos = multiplos + lista2
        i = i+1
	
    return multiplos