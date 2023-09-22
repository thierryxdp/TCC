def repetidos(lista):
    i=0
    y=0
    while i<len(lista):
        x=list.count(list,i)
        if y<x:
            y==x
        i=i+1
    return y