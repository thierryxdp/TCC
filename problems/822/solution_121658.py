def repetidos(lista):
    x=0
    count=0
    while x<=len(lista)-1:
        if lista[x+1]==lista[x]:
            count=count+1
        x=x+1
    return count