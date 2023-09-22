def acima_da_media(x):
    list.sort(x)
    y=sum(x)
    z=(sum(x))/len(x)
    p=list.index(x,z)
    return x[p:]