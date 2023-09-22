def repetidos(listadenumeros):
    indice = 0
    quantidade = 0
    while indice < len(listadenumeros):
        if listadenumeros[indice] == listadenumeros[indice+1]:
            quantidade +=1
        indice +=1
    return quantidade