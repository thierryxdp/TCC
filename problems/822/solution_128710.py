def repetidos(lista):
    l=lista[1:]
    b=[]
    t=list(range(len(lista)))
    for z in t:
        for x in list(range(len(l))):
            if lista[int(z)]==l[int(z)]:
                b.append(x)
    return b