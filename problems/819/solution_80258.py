def filtraMultiplos(x,n):
    i = 0
    listaFinal = []
    while i < len(x):
        if x[i]%n == 0:
            list.append(listaFinal,x[i])
        i += 1
    return x