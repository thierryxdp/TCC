def repetidos(lista_números):
    cont=+1
    rep=0
    while cont<len(lista_números)-1:
        if lista_números[cont]==lista_números[cont+1]:
            rep=rep+1
        cont=cont+1
    return rep