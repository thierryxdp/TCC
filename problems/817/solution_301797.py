def maiores(a,n):
    list.sort(a)
    lista=[]
    for i in a:
        if i>n:
            lista.append(i)
    return lista
def acima_da_media(b):
    media=sum(b)/len(b)
    
    return maiores(b,media)