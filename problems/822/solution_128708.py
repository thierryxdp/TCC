def repetidos(lista):
    l=lista[1:]
    b=[]
    t=list(range(len(lista)))
    for x in range(len(l)):
        for z in t:
            if lista[int(z)]==l[int(z)]:
                b.append(x)
    return b