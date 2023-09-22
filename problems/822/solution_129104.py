def repetidos(lista_numeros):
    cont=1
    rep=0
    while cont<len(lista_numeros)-1:
        if lista_numeros[cont]==lista_numeros[cont+1]:
            rep+=rep
        cont+=cont
    return rep