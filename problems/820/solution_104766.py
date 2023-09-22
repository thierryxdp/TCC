def posletra(string,letra,numero):
    cont=0
    lista=0
    while cont<len(string):
       if string[cont]==letra:
            lista = lista +1
            if lista = numero:
                return cont
        cont-cont +1
    return -1