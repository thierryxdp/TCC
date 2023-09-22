def maiores(lista,n):
    x=[]
    for y in lista:
        if y>n:
            list.append(x,y)
            list.sort(x)
    return x
def media(k):
    return sum(k)/len(k)
def acima_da_media(y):
    j=maiores(y,media(y))
    list.sort(j)
    return j