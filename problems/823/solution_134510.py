def faltante(lista):
    list.sort(lista)
    N = len(lista) + 1
    listacompleta = []
    y = 0
    while y < len(lista):
        listacompleta = listacompleta + [lista[y]]
        y = y + 1
    x = 1
    while x <= N:
        if x in listacompleta:
            x = x + 1
        else:
            return x