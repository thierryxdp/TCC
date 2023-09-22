def repetidos(lista):
    cont=1
    igual=0
    while cont<len(lista):
        if lista[cont]==lista[cont-1]:
            igual+=1
        cont+=1
    return igual