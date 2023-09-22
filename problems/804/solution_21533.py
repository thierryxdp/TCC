def filtra_pares(t):
    lista1= t
    lista = []
    a= t[:]
    for a in lista1 :
        if a % 2 == 0:
            lista.append(a)
            return tuple(lista)