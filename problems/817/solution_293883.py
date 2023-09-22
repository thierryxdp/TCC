def acima_da_media(l):
    ''''''
    A= sum(l)/len(l)+1
    list.sort(l)
    x=list.index(l,A)
    l[0:x+1]=[]
    return l