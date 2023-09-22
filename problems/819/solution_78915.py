def filtraMultiplos(lista,n):
    'list, int ->list'
    for i in lista[::]%n:
        return i