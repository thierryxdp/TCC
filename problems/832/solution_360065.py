def eh_quadrada(x):
    n=len(x)
    z=0
    for i in x:
        if len(i)!=n:
            z=z+1
    if z>0:
        return False
    else:
        return True