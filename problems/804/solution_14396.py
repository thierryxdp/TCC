def filtra_pares(tupla):
    tupla = (a,b,c,d)
    tupla1 = ()
    if int(tupla[0])%2==0:
        tupla1 = tupla1 + (tupla[0],)
    if int(tupla[1])%2==0:
        tupla1 = tupla1 + (tupla[1],)
    if int(tupla[2])%2==0:
        tupla1 = tupla1 + (tupla[2],)
    if int(tupla[3])%2==0:
        tupla1 = tupla1 + (tupla[3],)
        return tupla1