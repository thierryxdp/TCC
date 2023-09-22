def repetidos(lista):
    l=lista[1:]
    b=[]
    for x in lista:
        for y in l:
            if y == x:
                b.append(y)
    return len(b)