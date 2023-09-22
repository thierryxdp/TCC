def freq_palavras (frase):
    '''recebe uma string e retorna um dicionario com o número de vezes em que essa palavra aparece'''
    '''str->dicionario'''
    parte= str.split (frase)
    final= {}
    for palavra in parte:
        um = list.count(parte, palavra)
        final[palavra]=um
           
    return final