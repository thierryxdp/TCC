def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    tuplaVazia = ()
    if a%3==0:
        return
    elif b%3!=0:
        return tuplaVazia+(a,)+(b,)
    else:
        return tupla Vazia+(a,)+(b,)+(c,)+(d,)