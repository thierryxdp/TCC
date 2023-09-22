def repetidos(lista):
    l=lista[1:]
    b=[]
    t=int
    for x in l:
        for y in l:
            if y[(t)]== x[(t)]:
                b.append(y)
    return len(b)