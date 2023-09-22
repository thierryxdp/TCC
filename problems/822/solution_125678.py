def repetidos(listaX):
    """Função que receba uma lista de números, e retorne o número
    de vezes ocorre uma série de números iguais.list -> int"""
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaX[j-1]):
            listaR.count(listaX[j])
            cont += 1
        j += 1
    return cont