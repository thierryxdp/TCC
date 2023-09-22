def busca(x,y):
    b=[]
    for z in y:
        if x in z:
            z.remove(x)
            b.append(z)
    return b