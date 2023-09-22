def busca(x,y):
    b=[]
    for z in y:
        if x in z:
            b.append(z.del(2))
    return b