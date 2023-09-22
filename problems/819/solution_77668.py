def filtraMultiplos(lista,n):
    multiplos = ()
    num = 0
    while num > 0:
        if lista[num] / n:
            multiplos = multiplos + lista[num]
        num = num + 1
    return multiplos