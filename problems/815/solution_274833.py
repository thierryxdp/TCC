def eh_ordenada(lista):
    t=len(lista)
    l1=lista[:]
    l2=lista[:]
    c=list.sort(l2)
    l3=l2[:]
    d=list.reverse(l3)
    if t=1 and l1[0]==l2[0]:
        if t>=2 and l1[t-1]==c[t-1]:
            tu=(True,"crescente")
            return tu
        tu=(True,"crescente")
        return tu 
    elif t=1 and l1[0]!=l2[0]:
        if t>=2 and l1[0]==l2[t-1]:
            tu=(True,"decrescente")
            return tu
        tu=(False,"desordenada")
        return tu
    else:
        tu=(False,"desordenada")
        return tu