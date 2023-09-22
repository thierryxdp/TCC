def filtraMultiplos(lista, n):
  
    i = 0
    Mtp = []
    while i < len(lista):
        if lista[i] % n == 0:
            l = lista[i]
            Mtp.append(l)
        i += 1
    return Mtp