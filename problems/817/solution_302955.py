def ordena(x):
    return sorted(x)

def acima_da_media(x):
    t=len(x)
    z=(sum(ordena(x)))/t
    return x[z:]