def filtra_pares(tupla):
    a,b,c,d=(tupla)
    nova_tupla=()
    if a%2==0:
        nova_tupla += (a,)
    if b%2==0:
        nova_tupla += (b,)
    if c%2==0:
        nova_tupla += (c,)
    if d%2==0:
        nova_tupla += (d,)
    return nova_tupla#Start your python function here