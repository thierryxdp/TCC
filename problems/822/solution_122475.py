def repetidos(listanum):
    i=0
    igual=0
    while i<len(listanum):
        if lista[i]==lista[(i+1)]:
            igual=igual+1
        i=i+1
    return igual