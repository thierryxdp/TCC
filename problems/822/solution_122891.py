def repetidos(listaR):
    '''Funcao que receba uma lista de numeros, e retorne o numero
    de vezes ocorre uma serie de numeros iguais.
    list -> int'''
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont