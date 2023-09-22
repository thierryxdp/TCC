def filtra_pares(a,b,c,d):
    '''Função que recebe 4 valores numeros inteiros pares
    e retorna os numeros pares na ordem de entrada dos 
    valores.int,int,int,int->(int)(se houver)'''
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return a,b,c,d
    if a%2==0 and b%2==0 and c%2==0 and not d%2==0:
        return a,b,c
    if a%2==0 and b%2==0 and not c%2==0 and not d%2==0:
        return a,b
    if a%2==0 and not b%2==0 and not c%2==0 and not d%2==0:
        return a,
    if a%2!=0 and b%2==0 and not  c%2==0 and not d%2==0:
        return b,
    if a%2!=0 and not b%2==0 and  c%2==0 and not d%2==0:
        return c,
    if a%2!=0 and b%2==0 and  c%2==0 and d%2==0:
        return b,c,d
    if a%2!=0 and not b%2==0 and  c%2==0 and d%2==0:
        return c,d
    if a%2!=0 and not b%2==0 and not c%2==0 and d%2==0:
        return d,
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