def repetidos(listaR):
    """Função que receba uma lista de números, e retorne o número
    de vezes ocorre uma série de números iguais."""
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont