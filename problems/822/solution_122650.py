def repetidos(lista):
    i=0
    cont=0
    while i<len(lista):
        a=lista[i]
        b=lista[i+1]
        i+=1
        if(a==b):
            cont+=1
    return cont