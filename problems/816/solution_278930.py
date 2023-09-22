def maiores(lista, n):
    """Recebe uma lista e um número inteiro, e retorna apenas
    os valores maiores que n.
    list, int -> list"""
    
    list.append (lista, n)
    list.sort (lista)
    inicio = (list.index(lista, n) + 1)
    return lista[inicio:]