#Start your python function here
def filtrar_pares(t):
    t2=()
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    if a%2==0:
        t2=t2+(a,)
    if b%2==0:
        t2=t2+(b,)
    if c%2==0:
        t2=t2+(c,)
    if d%2==0:
        t2=t2+(d,)
    return tuple(t2)