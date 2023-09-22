def filtraMultiplos(ls, n):
    list=[]
    for x in ls:
        if x%n == 0:
            list.append(x)
    return list