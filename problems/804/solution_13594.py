def filtra_pares(a,b,c,d):
    tupla = ('a','b','c','d')
    tupla1 = ()
    if a%2==0:
        tupla1 = tupla1 + (tupla[0],)
        if b%2==0:
            tupla1 = tupla1 + (tupla[1],)
            if c%2==0:
                tupla1 = tupla1 + (tupla[2],)
                if d%2==0:
                    tupla1 = tupla1 + (tupla[3],)
                    return tupla1