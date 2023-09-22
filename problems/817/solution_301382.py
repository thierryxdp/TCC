def acima_da_media(x):
    m=sum(x)/len(x)
    list.append(x,m)
    list.sort(x)
    z=len(x)
    y=list.index(x,m)
    return x[y+1:z]