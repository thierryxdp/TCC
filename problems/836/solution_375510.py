def busca(x,y):
    b=[]
    for z in y:
        if x in z:
            b.append(z-z[2])
    return b