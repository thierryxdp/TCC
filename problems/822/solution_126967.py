def repetidos(lista):
    listaQ= 0
    indice= 0
    while indice<=(len(lista)-2):
        if lista[indice]==lista[indice +1]:
            listaQ= listaQ + 1
        indice= indice + 1
            
    return listaQ