def repetidos(lista):
    cont=0
    num=0
    tot=len(lista)
    while cont<tot:
        if cont>0 and lista[cont]==lista[cont-1]:
            num=num+1
        cont=cont+1
    return num