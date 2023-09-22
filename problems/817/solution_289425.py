from math import*
def acima_da_media(x):
    a=sum(x)/len(x)
    list.insert(x,0,a)
    list.sort(x)
    b=list.index(a)
    return x[b+1:]