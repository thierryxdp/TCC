def repetidos (lista):
    """ """
    proximo = ""
    atual = ""
    repetido = 0
    for i in lista:
        atual = lista[i]
        proximo = lista[i+1]
        if proximo == atual:
            repetido += 1
    
    return repetido