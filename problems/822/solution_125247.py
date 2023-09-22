def repetidos(lista):
    
    x = 0
    y = 0
    while x < len(lista):
        if lista[x-1] == lista[x]:
            y = y + 1
        x=x+1
    return y