def repetidos(lista):
    a=0
    for i in range(1,len(lista)):
        if lista[i]==lista[i-1]:
            a=a+1
    return a