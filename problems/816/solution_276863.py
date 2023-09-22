def maiores(numeros, n):
    """retorna os numeros maiores do que n"""
    lista = [list.sort(numeros)]
    p = list.index(lista, n)
    return lista[p:len(numeros)]