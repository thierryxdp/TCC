def acima_da_media(x):
    a=sum(x)/len(x)
    list.insert(x,0,a)
    list.sort(x)
    b=list.index(x,a)
    if x[b]==x[b+1]:
        return x[b+2:]
    else:
        return x[b+1:]