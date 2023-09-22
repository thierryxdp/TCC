def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.reverse()
    p=lista.index(n)
    listaf= lista[:p]
    listaf.sort()
    return listaf

def acima_da_media(nota):
    m=sum(nota)/len(nota)
    return maiores(nota,m)