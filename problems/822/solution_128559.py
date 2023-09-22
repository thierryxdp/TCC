def repetidos(lista_numeros):
    cont=1
    rep=0
    while cont<len(lista_numeros):
        if lista_numeros[cont]==lista_numeros[cont+1]:
            rep=rep +1
        cont=cont +1
    return rep