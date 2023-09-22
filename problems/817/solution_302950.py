def acima_da_media(x):
    m=sun(x)/len(x)
    list.append(x,m)
    list.sort(x)
    z=len(x)
    y=lis.index(x,m)
    return x[y+1:z]