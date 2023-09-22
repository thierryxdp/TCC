def filtraMultiplos(lista, n):
    """Dada uma lista de numeros e um numero, retorna uma lista com os numeros da lista original divisiveis por n
    list, int -> list"""
    t = []
    x = 0
    while x < len(lista):
        if lista[x]%n == 0:
            list.append(t, lista[x])
        elif lista[x]%n != 0:
            None
        x = x + 1
    return t