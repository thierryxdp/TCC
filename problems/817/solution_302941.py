def maiores (lista,n):
    x=[]
    for y in lista:
        if y>n:
            list.append(x,y)
            list.sort(x)
    return x
def media(y):
    return sum(y)/len(y)
def acima_da_media(x):
    i=maiores(x,media(x))
    list.sort(i)
    return i