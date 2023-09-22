def faltante(n):
    x=0
    z=1
    while len(n)-1>=n[x]:
        if n[0] == len(n)-1:
            return n[0] +1
        x=x+1
        z=z+1
    if z==len(n):
        return z+1
    else: return z