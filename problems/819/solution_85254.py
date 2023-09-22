def filtraMultiplos(ls,n):
    for i in ls:
        if i%n != 0:
            ls.remove(ls[i])
    return ls