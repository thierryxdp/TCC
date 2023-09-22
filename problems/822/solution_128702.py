def repetidos(lista):
    l=lista[1:]
    b=[]
    t=int
    for x in lista:
        for y in l:
            if range(y)== range(x):
                b.append(y)
    return len(b)