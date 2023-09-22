def filtraMultiplos(listan, n):
    '''...'''
    i= 0
    lista= [ ]
    while i< len(listan):
        if listan[i]%n==0:
            lista.append(listan[i])
            i=+ 1
    return lista