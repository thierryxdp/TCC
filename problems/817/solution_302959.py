def ordena(x):
    return sorted(x)

def acima_da_media(x):
    w=ordena(x)
    t=len(x)
    z=sum(w)//t
    r=w.index(z)
    return w[r:]