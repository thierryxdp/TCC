def posLetra (texto,letra,ocorrencia):
    '''dfgsd'''
    if str.count(texto,letra)>=ocorrencia:
        repeticoes=0
        indice_letra=0
        while repeticoes!=ocorrencia:
            indice_letra= str.find(texto,letra,indice_letra)
            repeticoes= repeticoes+1
        return indice_letra
    else:
        return-1