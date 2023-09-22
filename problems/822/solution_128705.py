def repetidos(lista):
    l=lista[1:]
    b=[]
    t=[range(len(lista))]
    for x in range(len(l)):
        for z in t:
            if lista[z]==l[z]:
                b.append(x)
    return b