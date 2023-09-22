def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    tuplaVazia = ()
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return tuplaVazia+(a,)+(b,)+(c,)+(d,)
    if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return tuplaVazia+(a,)+(b,)+(c,)
    if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return tuplaVazia+(a,)+(b,)+(d,)
    if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return tuplaVazia+(a,)+(c,)+(d,)
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return tuplaVazia+(b,)+(c,)+(d,)
    if a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return tuplaVazia+(a,)+(b,)
    if a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return tuplaVazia+(a,)+(c,)
    if a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return tuplaVazia+(b,)+(c,)
    if a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return tuplaVazia+(a,)+(d,)
    if a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return tuplaVazia+(b,)+(d,)
    if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return tuplaVazia+(c,)+(d,)
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

    




"""
def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    tuplaVazia = ()
    if a%2==0:
        return tuplaVazia+(a,)
    if b%2==0:
        return tuplaVazia+(b,)
    if c%2==0:
        return tuplaVazia+(c,)
    if d%2==0:
        return tuplaVazia+(d,)
    else:
        return tuplaVazia
"""