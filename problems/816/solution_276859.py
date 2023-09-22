def maiores(numeros, n):
    """retorna os numeros maiores do que n"""
    lista = [list.sort(numeros)]
    return lista[list.index(numeros, n):len(numeros)]