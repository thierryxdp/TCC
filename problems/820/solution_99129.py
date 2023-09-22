def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    i=str.find(texto,letra)
    while i>=0 and ocorrencia>1:
        i=str.find(letra,i+1)
        ocorrencia=ocorrencia-1
        return i