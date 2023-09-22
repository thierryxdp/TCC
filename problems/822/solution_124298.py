def repetidos(lista_numeros):
    """
    """
    vezes_repete=0
    i=0
    while i<len(lista_numeros)-1:
        if lista_numeros[i+1]==lista_numeros[i]:
            vezes_repete = vezes_repete + 1
        i=i+1
    return vezes_repete