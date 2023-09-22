def repetidos(listadenumeros):
    indice = 0
    quantidade = 0
    while indice <= (len(listadenumeros)-2):
        if listadenumeros[indice+1] == listadenumeros[indice]:
            quantidade +=1
        indice +=1
    
    return quantidade