def repetidos(n):
    z=0
    q=0
    while len(n)>z:
        if [z]==[z+1]:
            q=q+1
        z=z+1
    return q