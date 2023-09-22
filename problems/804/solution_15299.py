def filtra_pares(tupla):
    
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    for n in tupla:
        if n%2 == 0:
            return n,