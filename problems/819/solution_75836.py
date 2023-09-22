def filtraMultiplos(numeros, n):
    """essa funcao, dada uma lista de numeros e um numero n,
	 calcula e retorna uma lista contendo os multiplos de n"""
    multiplos = []
    p = 0
    while p < len(numeros)-1:
        if (numeros[p])%n == 0:
            multiplos = multiplos + [numeros[p],]
        p = p + 1
    return multiplos