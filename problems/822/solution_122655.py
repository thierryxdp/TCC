def repetidos(lista):
    i, cont, a, b=0, 0, 0, 0
    n=len(lista)-1
    while i<n:
        a=lista[i]
        i+=1
        b=lista[i]
        if(a==b):
            cont+=1
    return cont