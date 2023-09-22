def filtraMultiplos(ls,n):
    for i in range(len(ls)):
        if i%n != 0:
            ls.remove(i)
    return ls