def maiores(lista, n):
    mm = []
    idx = 0
    tam = len(lista)
    while idx < tam:
        el = lista[idx]
        if el > n:
       	    mm.append(el)
        idx += 1
    list.sort(mm)
    return mm