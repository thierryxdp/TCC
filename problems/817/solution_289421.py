from math import*
def acima_da_media(x):
    a=round(sum(x)/len(x))
    list.insert(x,0,a)
    list.sort(x)
    return x[a+1:]