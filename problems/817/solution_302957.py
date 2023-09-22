def ordena(x):
    return sorted(x)

def acima_da_media(x):
    w=ordena(x)
    t=len(x)
    z=w//t
    r=x.index(z)
    return w[r:]