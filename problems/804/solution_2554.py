def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    tuplaVazia = ()
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return tuplaVazia+(tupla[0:])
    if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return tuplaVazia+(tupla[0:3])
    if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return tuplaVazia+(tupla[0:2])+(d,)
    if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return tuplaVazia+(a,)+(tupla[2:])
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return tuplaVazia+(tupla[1:])
    if a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return tuplaVazia+(tupla[0:2])
    if a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return tuplaVazia+(a,)+(c,)
    if a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return tuplaVazia+(tupla[1:3])
    if a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return tuplaVazia+(a,)+(d,)
    if a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return tuplaVazia+(b,)+(d,)
    if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return tuplaVazia+(tupla[2:])
    if a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        return tuplaVazia+(d,)
    if a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return tuplaVazia+(c,)
    if a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return tuplaVazia+(b,)
    if a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return tuplaVazia+(a,)
    else:
        return tuplaVazia