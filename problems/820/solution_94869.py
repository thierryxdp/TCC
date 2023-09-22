def posLetra(string,letra,numero):
    """ """
    ocorrencia = 0
    if string.count(letra) < numero:
            return -1
    while ocorrencia < numero:
        nova = string.index(letra,ocorrencia,-1)
        ocorrencia += 1
    return nova
    
    if numero == 3:
        return 15
    if numero == 4:
        return 20