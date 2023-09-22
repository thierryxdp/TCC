def freq_palavras (frase):
    '''recebe uma string e retorna um dicionario com o número de vezes em que essa palavra aparece'''
    '''str->dicionario'''
    i = 0
    final = []
    while i < len(frase):
        if frase[i] in frase:
            um = str.count(frase, frase[i])
            final = um
            
        i = i+1
    return final