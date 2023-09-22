def repetidos(lista):
    x=1
    count=0
    while x<=len(lista)-1:
        if lista[x]==lista[x-1]:
            count=count+1
        x=x+1
    return count