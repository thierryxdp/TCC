def filtra_pares(a,b,c,d):
    tupla = a,b,c,d
    tupla1 = ()
    if a%2==0:
        tupla1 = tupla1 + (a,)
    if b%2==0:
        tupla1 = tupla1 + (b,)
    if c%2==0:
        tupla1 = tupla1 + (c,)
    if d%2==0:
        tupla1 = tupla1 + (d,)
        return tupla1