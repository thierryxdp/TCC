def maiores(ls,p):
    r=[]
    for e in ls:
        if e>p:
            list.append(r,e)
            list.sort(r)
    return r
def acima_da_media(lista):
    return maiores(lista,4)