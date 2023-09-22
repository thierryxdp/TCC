def repetidos(lista):
    i=0
    x=0
    while i < len(lista):
        if lista[i]==listalista[i-1]:
            x=x+1
        i=i+1
    return x