def filtraMultiplos(listanum,n):
    i = 0
    a = []
    while i < len(listanum):
        if listanum[i]%n!=0:
            a=listanum[i]
        i = i+1
    return a