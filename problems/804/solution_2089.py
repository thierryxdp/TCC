def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    A = a%2
    B = b%2
    C = c%2
    D = d%2
    tuplaVazia = ()
    if A==0 and B==0 and C==0 and D==0:
       return tuplaVazia+(a,)+(b,)+(c,)+(d,)
	if A==0 and B==0 and C==0 and D!=0:
       return tuplaVazia+(a,)+(b,)+(c,)
    if A==0 and B==0 and C!=0 and D==0:
       return tuplaVazia+(a,)+(b,)+(d,)
    if A==0 and B!=0 C==0 and D==0:
       return tuplaVazia+(a,)+(c,)+(d,)
    if A!=0 and B==0 and C==0 and D==0:
       return tuplaVazia+(b,)+(c,)+(d,)