def filtraMultiplos(listai,n):
    listaf = ()
    i = 0
    while i<len(listai):
        if listai[i]%n == 0:
            listaf= listaf + (listai[i],)
        i = i+1
    return list.listaf[]