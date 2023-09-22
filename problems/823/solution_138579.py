def faltante(n):
    x=0
    z=1
    while len(n)-1>=n[x]:
        if len(n)-1 ==x:
            return x+2
        elif n[x] +1 <= n[x+1]:
            return n[x]+1
        x=x+1
        z=z+1
    if z==n[len(n)-1]:
        return n[z+1]
    else: return z