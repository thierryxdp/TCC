#Start your python function here
def filtra_pares(tup):
    if tup[0]%2==0:
        a=(tup[0],)
    else:
        a=()
    if tup[1]%2==0:
        b=(tup[1],)
    else:
        b=()
    if tup[2]%2==0:
        c=(tup[2],)
    else:
        c=()
    if tup[3]%2==0:
        d=(tup[3],)
    else:
        d=()
    return (a+b+c+d)