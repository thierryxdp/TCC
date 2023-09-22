def filtra_pares(t):
    result=()
    e0=int(t[0])
    e1=int(t[1])
    e2=int(t[2])
    e3=int(t[3])
    if e0%2==0:
        result=result+(e0,)
    if e1%2==0:
        result=result+(e1,)
    if e2%2==0:
        result=result+(e2,) 
    if e3%2==0:
        result=result+(e3,)
    return result