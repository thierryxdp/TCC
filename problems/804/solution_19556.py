def filtra_pares(a,b,c,d):
    '''função que retorna apenas os elementos pares da tupla original(a,b,c,d= elementos inteiros)
      int,int,int,int->bool'''
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    tupla=()
    if a%2==0:
        tupla=tupla + (a,)
    if b%2==0:
        tupla=tupla + (b,)
    if c%2==0:
        tupla=tupla + (c,)
    if d%2==0:
        tupla=tupla + (d,)
    return tupla