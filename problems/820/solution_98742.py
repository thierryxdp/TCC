def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    i=0
    repeticoes=0
    while i<len(texto):
        while repeticoes>ocorrencia:
            if texto[i] == letra:
                repeticoes= repeticoes+1
                i=i+1
            elif texto[i]!= letra:
                i=i+1
        return str.find(texto,letra,i)