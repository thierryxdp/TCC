def acima_da_media(x):
    a=sum(x)/len(x)
    list.insert(x,0,a)
    list.sort(x)
    b=list.index(x,a)
    return x[b+1:]