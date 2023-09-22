def filtra_pares(tupla):
    """retorna os elementos impares da string. (tupla->tupla)"""
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
   
    return x
#Start your python function here