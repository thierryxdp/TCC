def filtra_pares(tupla):
    ''' recebe uma tupla com 4 elementos inteiros,
    retornando uma nova tupla contendo apenas os 
    elementos pares da tupla original.
    tuple -> tuple'''
    a=int(tupla[0])
    b=int(tupla[1])
    c=int(tupla[2])
    d=int(tupla[3])
    t=()
    if a%2==0:
        t=t+(a,)
    if b%2==0:
        t=t+(b,)
    if c%2==0:
        t=t+(c,)
        
    if d%2==0:
        t=t+(d,)
    return t