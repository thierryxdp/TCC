def freq_palavras (frase):
    '''recebera uma string e retornarar um dicional'''
    '''str->dicionario'''
    parte= str.split (frase)
    final= {}
    for palavra in parte:
        um = list.count (parte, palavra)
        final[palavra]=um

    return final