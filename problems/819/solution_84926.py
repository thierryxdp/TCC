def filtraMultiplos(numeros,n):
    dvs = ()
    for nmr in numeros:
        if nmr % n == 0:
            dvs.append(nmr)
            return dvs