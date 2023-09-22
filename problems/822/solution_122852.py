def repetidos(listaR):
    """Esta função recebe uma lista de números, e retorna o número
    de vezes que ocorre uma série de números iguais."""
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont