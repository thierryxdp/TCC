def maiores(numeros, n):
    """Funcao que retorna a lista "numeros", contendo apenas os numeros maiores que "n"
    list, int -> list"""
    a= numeros
    list.extend(numeros,[n])
    a.sort()
    b= list.index(a, n)
    return a[b+1:]