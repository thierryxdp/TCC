def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    x = (a,b,c,d)
    tuplaVazia = ()
    if x%2==0:
        return tuplaVazia+bool(x%2==0)==True
    else:
        return tuplaVazia