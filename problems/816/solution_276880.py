def maiores(numeros, n):
    """retorna os numeros maiores do que n"""
    list.sort(numeros)
    return numeros[list.index(numeros,n):len(numeros)]