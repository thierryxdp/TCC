def faltante(lista):
    list.sort(lista)
    i = 0
    while i < len(lista)+1:
        if 1 not in lista:
            return 1
        elif lista[i+1] - lista[i] > 1:
            return lista[i]+1
        else:
            return lista[-1]+1
        i += 1