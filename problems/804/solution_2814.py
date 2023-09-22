def filtra_pares(A):
    '''Filtra os pares da tupla recebida.
    tupla(int,int,int,int) -> tupla'''
    a=A[0]
    b=A[1]
    c=A[2]
    d=A[3]
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,)+(b,)+(c,)+(d,)
    if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return (a,)+(b,)+(c,)
    if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return (a,)+(b,)+(d,)
    if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,)+(c,)+(d,)
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return (b,)+(c,)+(d,)
    if a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,)+(b,)
    if a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,)+(c,)
    if a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return (b,)+(c,)
    if a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,)+(d,)
    if a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return (b,)+(d,)
    if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return (c,)+(d,)
    if a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return (a,)
    if a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return (b,)
    if a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return (c,)
    if a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        return (d,)
    if a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
        return ()