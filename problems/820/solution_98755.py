def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    i=0
    repeticoes=0
    while str.count(texto,letra)<ocorrencia:
        if repeticoes==ocorrencia:
            return str.find(texto,letra,i)
        elif repeticoes<ocorrencia:
            return -1
        else:
            i=str.find(texto,letra,i)
            repeticoes=repeticoes+1