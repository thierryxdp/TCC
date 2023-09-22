def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    tuplaVazia = ()
    if a%2==0:
       return tuplaVazia+(a,)+(b,)+(c,)+(d,)
    if b%2==0:
       return tuplaVazia+(b,)
    if c%2==0:
       return tuplaVazia+(c,)
    if d%2==0:
       return tuplaVazia+(d,)
    else:
       return tuplaVazia