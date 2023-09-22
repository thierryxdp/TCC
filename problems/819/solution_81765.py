def filtraMultiplos (lista_numero,n):
    novalista = []
    i = 0
    while i < len(lista_numero):
        if (lista_numero[i]%n == 0):
            novalista = novalista + [lista_numero[i]]
        i = i + 1
    return novalista