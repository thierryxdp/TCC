def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    i=0
    repeticoes=0
    while repeticoes<ocorrencia:
        if str.count(texto,letra)<ocorrencia:
            return-1
        else:
            i=str.find(texto,letra,i)
            repeticoes=repeticoes+1
    return  str.find(texto,letra,i)