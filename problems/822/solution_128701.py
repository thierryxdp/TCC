def repetidos(lista):
    l=lista[1:]
    b=[]
    t=int
    for x in lista:
        for y in range(l):
            if y == x:
                b.append(y)
    return len(b)