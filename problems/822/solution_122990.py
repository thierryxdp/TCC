def repetidos(listaNumeros):
    contador=0
    listaResultado=0
    while contador<len(listaNumeros):
        if listaNumeros[contador]==listaNumeros[contador-1]:
            listaResultado+=1
        else:
            pass
    contador+=1
    return listaResultado