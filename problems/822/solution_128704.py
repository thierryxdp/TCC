def repetidos(lista):
    l=lista[1:]
    b=[]
    t=[range(len(lista))]
    for x in range(len(l)):
        for y in range(len(l)):
            for z in t:
                if x[z]==y[z]:
                    b.append(x)
    return b