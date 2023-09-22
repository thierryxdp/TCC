def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    if str.count(texto,letra)>=ocorrencia:
        repeticoes=0
        i=0
        while not(repeticoes==ocorrencia):
            i= str.index(texto,letra,i)
            repeticoes= repeticoes+1
            return i
    else:
        return-1