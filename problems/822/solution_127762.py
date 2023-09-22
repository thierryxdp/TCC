def repetidos(lista):
    x=0
    i=0
    while i <len(lista):
        if lista[i]== lista [i-1]:
            x=x+1
            i=i+1
            return x