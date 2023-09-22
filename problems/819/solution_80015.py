def filtraMultiplos (listanum, num):
    n = 0
    listafinal = []

    while n < len(listanum):
        if listanum[n]%num == 0: 
            listafinal = listafinal + [ listanum[n] ]
            n = n + 1

        else:
            n += 1
            listafinal = listafinal

    return listafinal