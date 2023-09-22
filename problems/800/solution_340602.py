def total(lista,d):
    if len(lista)==4:
        a=lista[0]
        b=lista[1]
        c=lista[2]
        h=lista[3]
        preco=(d[a]+d[b]+d[c]+d[h])
        return preco
    
    elif len(lista)==7:
        a=lista[0]
        b=lista[1]
        c=lista[2]
        h=lista[3]
        e=lista[4]
        f=lista[5]
        g=lista[6]
        preco=(d[a]+d[b]+d[c]+d[h]+d[e]+d[f]+d[g])
        return preco
    elif len(lista)==6:
        a=lista[0]
        b=lista[1]
        c=lista[2]
        h=lista[3]
        e=lista[4]
        f=lista[5]
        preco=(d[a]+d[b]+d[c]+d[h]+d[e]+d[f])
        if preco==35,99:
            return 36
        else:
            return preco