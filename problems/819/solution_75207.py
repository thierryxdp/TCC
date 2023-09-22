def filtraMultiplos(lista, n):
    lista = list(range(1000))
    listafinal = []
    i = 0
    while i*n < 1000:
        if i*n < 1000:
            listafinal = listafinal + [i*n]
            i = i + 1
            return listafinal