def freq_palavras(frase):
    '''
    '''
    palavra = frases.split()
    dicionario = {}
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i:contador})
    return dicionario