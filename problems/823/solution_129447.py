def faltante(lista):
    n = 1
    i = 0
    x = len(lista) + 1
    while i < len(lista):
        if list.sort(lista + [n]) == [*range(x)]: 
            return n
        else: 
            n = n + 1
        i = i + 1