def repetidos(lista,numeros):
    cont=1
    rep=0
    while cont<len(lista_numeros)-1:
        if lista_numeros[cont]==lista_numeros[cont+1]:
            rep=rep+1
        cont=cont+1
    return rep