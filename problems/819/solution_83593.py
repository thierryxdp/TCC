def filtraMultiplos(lista, num):    
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % num == 0:
            m = lista[i]
            multiplos.append(m)
        i += 1
    return multiplos