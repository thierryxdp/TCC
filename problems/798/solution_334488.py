def freq_palavras (frase):
    '''recebe uma string e retorna um dicionario com o número de vezes em que essa palavra aparece'''
    '''str->dicionario'''
    parte= str.split (frase) 
    for palavra in parte:
        if palavra in frase:
            um = str.count(frase, palavra)
            final= {final[palavra]:um}
           
    return final