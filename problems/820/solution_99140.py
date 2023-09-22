def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    i=texto.find(letra)
    while i >=0 and ocorrencia> 1:
        i=texto.find(letra,i+1)
        ocorrencia=ocorrencia-1
    return i