def repetidos(n):
    z=0
    x=1
    q=0
    while len(n)>z:
        if n[x]==n[z]:
            q=q+1
        x=x+1
        z=z+1
    return q