def filtraMultiplos(numeros,n):
    dvs = list()
    for nmr in numeros:
        if nmr % n == 0:
            dvs.append(nmr)
            return dvs