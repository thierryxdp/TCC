def repetidos(lista):
    i, cont, a, b=0, 0, 0, 0
    while i<=len(lista):
        a=lista[i]
        i+=1
        b=lista[i]
        if(a==b):
            cont+=1
    return cont