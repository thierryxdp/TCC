def filtra_pares(a,b,c,d):
    '''Função que recebe uma tupla com 4 numeros int e entrega uma nova tupla 
    contendo apenas os elementos pares(se houver) da tupla original.tuple->tuple'''
    r1=(a,b,c,d)
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return r1
    if a%2==0 and b%2==0 and c%2==0 and not d%2==0:
        return a,b,c
    if a%2==0 and b%2==0 and not c%2==0 and not d%2==0:
        return a,b
    if a%2==0 and not b%2==0 and not c%2==0 and not d%2==0:
        return a
    if a%2!=0  and b%2==0  and not  c%2==0 and not d%2==0:
        return b
    if a%2!=0 and not b%2==0 and  c%2==0 and not d%2==0:
        return c
    if a%2!=0 and b%2==0 and  c%2==0 and d%2==0:
        return b,c,d
    if a%2!=0 and not b%2==0 and  c%2==0 and d%2==0:
        return c,d
    if a%2!=0 and not b%2==0 and not c%2==0 and d%2==0:
        return d
    if a%2!=0 and not b%2==0 and not c%2==0 and not d%2==0:
        return ()
    if a%2==0 and not b%2==0 and not c%2==0 and d%2==0:
        return a,d
    if a%2==0 and not b%2==0 and  c%2==0 and not d%2==0:
        return a,c
    if a%2!=0 and b%2==0 and  c%2==0 and not d%2==0:
        return b,c
    if a%2!=0 and b%2==0 and not c%2==0 and d%2==0:
        return b,d
    if a%2==0 and not b%2==0 and c%2==0 and d%2==0:
        return a,c,d
    if a%2==0 and  b%2==0 and not c%2==0 and d%2==0:
        return a,b,d