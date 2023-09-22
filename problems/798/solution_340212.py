def freq_palavras(frase):
    '''str -> dict'''
    ocorrencia = {}
    frase = frase.split(" ") 
    for palavra in frase:
        if palavra in ocorrencia:
            ocorrencia[palavra] += 1
        else :
            ocorrencia[palavra] = 1
    return ocorrencia