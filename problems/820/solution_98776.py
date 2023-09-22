def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    repeticoes=0
    i=0
    while not(repeticoes==ocorrencia):
        if str.count(texto,letra)<ocorrencias:
            return -1
        else:
            i=str.find(texto,letra,i)
            repeticoes=repeticoes+1
    return i