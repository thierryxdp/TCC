def filtra_pares(t):
    (a,b,c,d)=t
    lista = []
    for a in t :
        if a % 2 == 0:
            lista.append(a)
            return tuple(lista)