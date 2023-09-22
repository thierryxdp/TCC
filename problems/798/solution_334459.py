def freq_palavras (frase):
    '''recebe uma string e retorna um dicionario com o número de vezes em que essa palavra aparece'''
    '''str->dicionario'''
    i = 0
    for palavra in frase:
        if palavra in frase:
            str.count (palavra, frase)
            i= i+palavra    
    return i