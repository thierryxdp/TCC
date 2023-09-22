def repetidos(lista):
    i=0
    a=len(lista)
    b=0
    while i<a+1:
        if lista[i]==lista[i+1]:
            b=b+1
        i=i+1
    return b