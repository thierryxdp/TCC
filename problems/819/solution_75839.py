def filtraMultiplos(numeros, n):
    """essa funcao, dada uma lista de numeros e um numero n,
	 calcula e retorna uma lista contendo todos os elementos que forem multiplos de n
	list, int -> list"""
    
    multiplos = []
    p = 0
    while p < len(numeros):
        if (numeros[p])%n == 0:
            multiplos = multiplos + [numeros[p],]
        p = p + 1
    return multiplos