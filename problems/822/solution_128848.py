def repetidos(lista):
    x=0
    i=0
    for e in lista:
        if e==(lista[i-1]):
            x= x+1
            i= i+1
        else:
            x= x
            i =i+1
    return x