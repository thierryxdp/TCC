def freq_palavras(frases):
    '''retorna a frequencia que cada palavra aparece na frase
    str --> dict'''
    frequencia={}
    for palavra in frases:
        frequencia[palavra:str.count(frases,palavra)]
    return frequencia