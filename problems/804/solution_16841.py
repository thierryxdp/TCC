def filtra_pares(a,b,c,d):
    lista = []
    tupla = (a,b,c,d)
    for n in tupla:
        if n%2 == 0:
            lista.append(n)
            tupla2 = tuple(lista)
            print(tupla2)