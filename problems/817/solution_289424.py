from math import*
def acima_da_media(x):
    a=sum(x)/len(x)
    list.insert(x,0,a)
    b=list.sort(x)
    return x[b+1:]