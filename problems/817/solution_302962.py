def ordena(x):
    return sorted(x)

def acima_da_media(x):
    r=[]
    w=ordena(x)
    t=len(x)
    z=sum(w)//t
    for i in w:
        if i>=z:
            r.append(i)
    return r