def repetidos(lista):
    x=0
    count=0
    lista.split()
    while x<=len(lista):
        lista[x]=lista[x+1]
        count=count+1
        x=x+1
    return count