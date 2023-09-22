def faltante(n):
    x=0

    while len(n)-1>=n[x]:
        if x+1!=n[x]:
            return x +1
        x=x+1
    elif x>n:
        return x + 1