def repetidos(lista):
    i=0
    cont=0
    while i<len(lista):
        a=lista[i]
        i+=1
        b=lista[i]
        if(a==b):
            cont+=1
    return cont