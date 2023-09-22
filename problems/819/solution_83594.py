def filtraMultiplos(lista, num):
  
    i = 0
    M = []
    while i < len(lista):
        if lista[i] % num == 0:
            l = lista[i]
            M.append(l)
        i += 1
    return