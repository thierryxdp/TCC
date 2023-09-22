def maiores(numeros, n):
    """Recebe uma lista e um número inteiro, e retorna uma lista com valores maiores que n.
    	List, int -> list"""
    maiores =[]
    numeros.sort()
    for i in range (0, len(numeros)):
        if numeros[i] > n:
            maiores.append(numeros[i])
    return maiores