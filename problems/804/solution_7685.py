#Start your python function here
def filtra_pares (n):
    ''' dado uma tupla de 4 elementos inteiros, retorna uma nova tupla somente com pares.
    entrada: n -> int
    saida: '''
    a=int(n[0])
    a1 = a%2
    b=int(n[1])
    b1=b%2
    c=int(n[2])
    c2 = c%2
    d=int(n[3])
    d1=d%2
    tupla = ()
    if a1 == 0 :
        tupla = tupla + (a,)
    if b1 == 0:
        tupla = tupla + (b,)
    if c1 == 0:
        tupla = tupla + (c,)
    if d1 == 0:
        tupla = tupla + (d,)
    return tupla