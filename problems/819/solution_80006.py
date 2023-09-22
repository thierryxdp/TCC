def filtraMultiplos (listanum, num):
    n = 0
    listafinal = []

    while n < len(listanum):
        if listanum[n]%num == 0:
            n = n + 1
            listafinal = listafinal + [ listanum[n] ]

        else:
            n += 0
            listafinal = listafinal
    return listafinal