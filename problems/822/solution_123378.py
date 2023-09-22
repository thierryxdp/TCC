def repetidos(lista):
    cont=1
    cont2=0
    while cont-1<=len(lista):
        cont=cont+1
        if lista[cont]==lista[cont-1]:
            cont2=cont2+1
    return cont2