def filtraMultiplos(lista, x) :
    multi = []
    i = 0
    while i <= len(lista):
        if lista[i]%x == 0 :
            multi.append(lista[i])
        i += 1