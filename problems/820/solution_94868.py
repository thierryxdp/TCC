def posLetra(string,letra,numero):
    """ """
    ocorrencia = 0
    if string.count(letra) < numero:
            return -1
    while ocorrencia < numero:
        nova = string.index(letra,ocorrencia,-1)
        ocorrencia += 1
    return nova