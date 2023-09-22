def filtraMultiplos(lista,n):
    for i in lista:
        if i%n == 0:
            print(n, end='')