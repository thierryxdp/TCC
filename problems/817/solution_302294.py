def maiores(l,n):
    l.sort()
    a=[]
    for i in range(len(l)):
        if l[i]>n:
            a.append(l[i])
    return a 

def acima_da_media(l,n):
    maiores(l,n)